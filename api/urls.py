from django.conf.urls import url, include
from rest_framework.authtoken import views

from .views import ProductView, CategoryView


urlpatterns = [
    url(r'^products/', ProductView.as_view(), name='product'),
    # url(r'^products/new/', ProductCreateView.as_view(), name="product-create"),
    url(r'^categories/', CategoryView.as_view(), name='category'),
    # url(r'^users/', UserList.as_view(), name='user'),


    # url(r'^auth/', views.obtain_auth_token),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),
    url(r'^registration/verify-email/', include('rest_auth.registration.urls'))
]
