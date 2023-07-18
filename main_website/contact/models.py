from django.db import models
from django.utils import timezone


# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=500)
    submitted_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name

