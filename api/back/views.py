from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django import forms
from django.conf import settings

from rest_hooks.models import Hook

from . import models
from rest_framework.authtoken.models import Token
from . import serializers

class CourierView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = models.Courier.objects.all()
    serializer_class = serializers.CourierSerializer

class VendorView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer

class CustomerView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

class OrderView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    #
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class HookView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Hook.objects.all()
    serializer_class = serializers.HookSerializer
