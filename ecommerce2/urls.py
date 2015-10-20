from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from carts.views import CartView, ItemCountView, CheckoutView, CheckoutFinalView
from orders.views import AddressSelectFormView, UserAddressCreateView, OrderList
from products.views import CategoryListAPIView

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
    url(r'^api/categories/$', CategoryListAPIView.as_view(), name="categories_api"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
