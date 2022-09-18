from django.db import models


class Item(models.Model):
    text = models.TextField()


class List(models.Model):
    pass

# Create your models here.
