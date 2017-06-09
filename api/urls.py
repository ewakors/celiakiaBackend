from django.conf.urls import url, include
from rest_framework.authtoken import views

from .views import ProductView, CategoryView, ProductCreateView, ImageView


urlpatterns = [
    url(r'^products/$', ProductView.as_view(), name='product'),
    url(r'^products/new/$', ProductCreateView.as_view(), name="product_new"),
    url(r'^categories/', CategoryView.as_view(), name='category'),
    url(r'^images/', ImageView.as_view(), name='image'),

    url(r'^auth/', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls'))
]
