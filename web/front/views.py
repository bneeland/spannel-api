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

        url = "http://api:8001/api/orders"

        headers = {
          'Authorization': 'Token b34ce6532d8614bae62f72b8a106d66b1b2e2b3a'
        }

        response = requests.request("GET", url, headers=headers)

        context['orders'] = response.json()
        return context
