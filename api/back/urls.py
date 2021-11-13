from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_namespace = 'back'

router = routers.DefaultRouter(trailing_slash=False)
router.register('couriers', views.CourierView)
router.register('vendors', views.VendorView)
router.register('customers', views.CustomerView)
router.register('orders', views.OrderView)
router.register('hooks', views.HookView)

urlpatterns = [
    path('', include(router.urls)),
    path('token', obtain_auth_token, name='obtain_auth_token'),
]
