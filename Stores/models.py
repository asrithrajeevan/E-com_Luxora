from django.db import models

# Create your models here.

class Items(models.Model):
    item_name = models.CharField(max_length=255)
    item_rate = models.CharField(max_length=255)
    item_image = models.ImageField(upload_to='items')

class User(models.Model):
    user_firstname = models.CharField(max_length=255)
    user_lastname = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_dob = models.DateField()
    user_gender = models.CharField(max_length=255)
    user_phone = models.BigIntegerField()
    alt_phone = models.BigIntegerField()
    user_pin = models.CharField(max_length=255)
    user_place = models.CharField(max_length=255)
    user_country = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_address = models.CharField(max_length=255)