from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from . import models

class Home(SuccessMessageMixin, CreateView):
    model = models.Subscriber
    fields = [
        'first_name',
        'last_name',
        'email',
        'reason',
    ]
    template_name = 'front/home.html'
    success_url = reverse_lazy('front:home')
    success_message = "Thanks, %(first_name)s. We'll be in touch to get you started with Spannel, and with occasional updates."
