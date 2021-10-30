from django.urls import path, include

from . import views

app_namespace = 'front'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_view'),
    path('api', views.DashboardView.as_view(), name='dashboard_view'),
]
