from django.db import models



# Create your models here.
class Product(models.Model):
    Title = models.CharField(max_length=254)
    Description = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Inventory_Quantity = models.IntegerField()