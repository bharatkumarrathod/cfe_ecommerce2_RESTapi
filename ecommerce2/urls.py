from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from carts.views import CartView, ItemCountView, CheckoutView, CheckoutFinalView
from orders.views import AddressSelectFormView, UserAddressCreateView, OrderList
from products.views import (
                            CategoryListAPIView,
                            CategoryRetrieveAPIView,
                            ProductListAPIView,
                            ProductRetrieveAPIView,
                            # ProductCreateAPIView,
                            APIHomeView,
                            )

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/', 'newsletter.views.contact', name='contact'),
    url(r'^message_submitted/', 'newsletter.views.message_submitted', name='contact_us_submitted'),
    url(r'^sign-up-successful/', 'newsletter.views.sign_up_successful', name='sign_up_successful'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^categories/', include('products.urls_categories')),
    url(r'^orders/$', OrderList.as_view(), name="orders"),
    url(r'^cart/$', CartView.as_view(), name="cart"),
    url(r'^cart/count/$', ItemCountView.as_view(), name="item_count"),
    url(r'^checkout/$', CheckoutView.as_view(), name="checkout"),
    url(r'^checkout/address/$', AddressSelectFormView.as_view(), name="order_address"),
    url(r'^checkout/address/add/$', UserAddressCreateView.as_view(), name="user_address_create"),
    url(r'^checkout/final/$', CheckoutFinalView.as_view(), name="checkout_final"),

    # API URLS
    url(r'^api/auth/token/$', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/$', APIHomeView.as_view(), name="home_api"),
    url(r'^api/categories/$', CategoryListAPIView.as_view(), name="categories_api"),
    url(r'^api/categories/(?P<pk>\d+)/$', CategoryRetrieveAPIView.as_view(), name="category_detail_api"),
    url(r'^api/products/$', ProductListAPIView.as_view(), name="products_api"),
    url(r'^api/products/(?P<pk>\d+)/$', ProductRetrieveAPIView.as_view(), name="product_detail_api"),
    # url(r'^api/products/create/$', ProductCreateAPIView.as_view(), name="product_create_api"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
