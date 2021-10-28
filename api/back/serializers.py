from django.conf import settings
from rest_framework import serializers, exceptions

from rest_hooks.models import Hook

from . import models

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Courier
        fields = (
            'uuid',
            'first_name',
            'last_name',
            'email',
            'vehicle_class',
            'vehicle_make',
            'vehicle_model',
            'vehicle_year',
            'orders_completed',
            'score',
            'city',
            'country',
            'is_active',
            'created_at',
            'modified_at',
        )

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = (
            'uuid',
            'first_name',
            'last_name',
            'email',
            'business_name',
            'address',
            'city',
            'province',
            'postal_code',
            'country',
            'is_active',
            'created_at',
            'modified_at',
        )

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = (
            'uuid',
            'first_name',
            'last_name',
            'email',
            'address',
            'city',
            'province',
            'postal_code',
            'country',
            'is_active',
            'created_at',
            'modified_at',
        )

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = (
            'uuid',
            'item_type',
            'item_value',
            'pickup_date',
            'pickup_time',
            'dropoff_date',
            'dropoff_time',
            'trip_distance',
            'courier',
            'vendor',
            'customer',
            'created_at',
            'modified_at',
            'acknowledged_at',
            'picked_up_at',
            'delivered_at',
            'completed_at',
        )

class HookSerializer(serializers.ModelSerializer):
    def validate_event(self, event):
        if event not in settings.HOOK_EVENTS:
            err_msg = "Unexpected event {}".format(event)
            raise exceptions.ValidationError(detail=err_msg, code=400)
        return event

    class Meta:
        model = Hook
        fields = '__all__'
        read_only_fields = ('user',)
