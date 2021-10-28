from django.urls import path, include

from . import views

app_namespace = 'front'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]
