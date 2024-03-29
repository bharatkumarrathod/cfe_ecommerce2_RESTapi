from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse as api_reverse
from rest_framework.views import APIView

from .mixins import StaffRequiredMixin
from .models import Product, Variation, Category
from .forms import VariationInventoryFormSet
from products.filters import ProductFilter
from products.pagination import ProductPagination, CategoryPagination
from products.serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer, \
    ProductDetailUpdateSerializer


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        instance = self.get_object()
        context["related"] = Product.objects.get_related(instance)[:6]
        return context


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context["now"] = timezone.now()
        context["query"] = self.request.GET.get("q")
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        return qs


# Old style Function based view. Example only.
"""
def product_detail_view(self, request, pk):
        product_instance = Product.objects.get(pk=pk)
        template = 'products/product_detail.html'
        context = {
            'object': product_instance
        }
        return render(request, template, context)
"""


class VariationListView(StaffRequiredMixin,ListView):
    model = Variation
    queryset = Variation.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(VariationListView, self).get_context_data(*args, **kwargs)
        context["formset"] = VariationInventoryFormSet(queryset=self.get_queryset())
        return context

    def get_queryset(self, *args, **kwargs):
        product_pk = self.kwargs.get("pk")
        if product_pk:
            product = get_object_or_404(Product, pk=product_pk)
            queryset = Variation.objects.filter(product=product)
        return queryset

    def post(self, request, *args, **kwargs):
        formset = VariationInventoryFormSet(request.POST, request.FILES)
        # print(request.POST)
        if formset.is_valid():
            formset.save(commit=False)
            for form in formset:
                new_item = form.save(commit=False)
                if new_item.title:
                    product_pk = self.kwargs.get("pk")
                    product = get_object_or_404(Product, pk=product_pk)
                    new_item.product = product
                    new_item.save()
            messages.success(request, "Your inventory has successfully been updated.")
            return redirect('products')
        raise Http404


class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "products/product_list.html"


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self,*args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        instance = self.get_object()
        product_set = instance.product_set.all()
        default_products = instance.default_category.all()
        products = (product_set | default_products).distinct()
        context["products"] = products
        return context

# API Views


class APIHomeView(APIView):

    def get(self, request, format=None):
        data = {
            'products': {
                'count': Product.objects.all().count(),
                'url': api_reverse('products_api')
            },
            'categories': {
                'count': Category.objects.all().count(),
                'url': api_reverse('categories_api')
            }
        }
        return Response(data)


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CategoryPagination


class CategoryRetrieveAPIView(RetrieveAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        filters.DjangoFilterBackend
                       ]
    search_fields = ["title", "description"]
    ordering_fields = ["id", "title"]
    filter_class = ProductFilter
    # pagination_class = ProductPagination


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


# class ProductCreateAPIView(CreateAPIView):
#     serializer_class = ProductDetailUpdateSerializer
#     queryset = Product.objects.all()
