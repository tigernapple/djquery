#/usr/bin/python 
#coding: utf8
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100,unique=True)
    description    = models.TextField()
    image_url = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    date_available = models.DateField()
    #orders = models.ManyToManyField(Order,through='LineItem')

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品"
