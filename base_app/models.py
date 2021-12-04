from django.db import models

# Create your models here.

class Film(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    video = models.FileField()

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title