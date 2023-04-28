from django.db import models

# Create your models here.

class Items(models.Model):
    item_name = models.CharField(max_length=255)
    item_rate = models.CharField(max_length=255)
    item_image = models.ImageField(upload_to='items')