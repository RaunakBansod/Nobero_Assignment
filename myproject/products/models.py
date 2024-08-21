from django.db import models

class Product(models.Model):
    category = models.CharField(max_length=255)
    url = models.URLField()
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    MRP = models.DecimalField(max_digits=10, decimal_places=2)
    last_7_day_sale = models.DecimalField(max_digits=10, decimal_places=2)
    available_skus = models.JSONField()
    fit = models.CharField(max_length=255)
    fabric = models.CharField(max_length=255)
    neck = models.CharField(max_length=255)
    sleeve = models.CharField(max_length=255)
    pattern = models.CharField(max_length=255)
    length = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   