from django.conf.urls import url
from .views import ProductDetailView, ProductListView, VariationListView


urlpatterns = [
    # url(r'^(?P<pk>\d+)', 'products.views.product_detail_view', name='product_detail_view'),
    url(r'^$', ProductListView.as_view(), name='products'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^(?P<pk>\d+)/inventory/$', VariationListView.as_view(), name='product_inventory'),
]
