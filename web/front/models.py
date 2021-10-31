from django.db import models
from django.conf import settings

class Key(models.Model):
    token = models.CharField(max_length=40, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="%(app_label)s_%(class)s_related", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
