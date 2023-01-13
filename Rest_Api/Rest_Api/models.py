from django.db import models

# create an class to initialize the models
class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    