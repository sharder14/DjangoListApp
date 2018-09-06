from django.db import models

# Create your models here.

class Food(models.Model):
    foodname = models.CharField(max_length=200)
    def __str__(self):
        return self.foodname

class List(models.Model):
    item = models.CharField(max_length=200)

    def __str__(self):
        return self.item