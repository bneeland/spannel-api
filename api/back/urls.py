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

urlpatterns = [
    path('', include(router.urls)),
    path('token', obtain_auth_token, name='obtain_auth_token'),
    # path('settings', views.Settings.as_view(), name='settings'),
    # path('settings/webhooks/create', views.CreateWebhook.as_view(), name='create_webhook'),
    # path('settings/webhooks/<int:pk>/update', views.UpdateWebhook.as_view(), name='update_webhook'),
    # path('settings/webhooks/<int:pk>/delete', views.DeleteWebhook.as_view(), name='delete_webhook'),
]
