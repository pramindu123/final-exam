from django.db import models

# Create your models here.
class Product(models.Model):
    pname = models.CharField(max_length=100)  
    description = models.TextField()  
    category = models.CharField(max_length=50)  
    price = models.DecimalField(max_digits=8, decimal_places=2) 

    def __str__(self):
        return self.pname

class Review(models.Model):
    username = models.CharField(max_length=100)  
    comment = models.TextField()  
    def __str__(self):
        return self.username
