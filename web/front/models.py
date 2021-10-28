from django.db import models

class Subscriber(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    reason = models.TextField(blank=True, null=True, verbose_name="What do you want to achieve with Spannel?")

    def __str__(self):
        return self.email
