from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

class HomeView(TemplateView):
    template_name = 'front/home_view.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'front/dashboard_view.html'
