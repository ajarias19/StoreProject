from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    amount = models.IntegerField()
    Description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.name