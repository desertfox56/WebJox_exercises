from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.FileField(upload_to='products/')
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE)
