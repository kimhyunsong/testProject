from django.db import models
from django.utils import timezone
# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=255, blank=False)
    start_date = models.DateTimeField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)