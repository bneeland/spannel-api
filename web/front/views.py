from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

import requests

from . import models

class HomeView(TemplateView):
    template_name = 'front/home_view.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'front/dashboard_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        key = models.Key.objects.get(user=self.request.user).token

        context['key'] = key

        headers = {
          'Authorization': 'Token ' + key
        }

        # Orders
        url = "http://api:8001/api/orders"
        response = requests.request("GET", url, headers=headers)
        context['orders'] = response.json()

        # Vendors
        url = "http://api:8001/api/vendors"
        response = requests.request("GET", url, headers=headers)
        context['vendors'] = response.json()

        # Couriers
        url = "http://api:8001/api/couriers"
        response = requests.request("GET", url, headers=headers)
        context['couriers'] = response.json()

        # Customers
        url = "http://api:8001/api/customers"
        response = requests.request("GET", url, headers=headers)
        context['customers'] = response.json()

        return context
