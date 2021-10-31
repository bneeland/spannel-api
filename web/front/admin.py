from django.contrib import admin

from . import models

class KeyAdmin(admin.ModelAdmin):
    list_display = ('token', 'user', 'created_at', )

admin.site.register(models.Key, KeyAdmin)
