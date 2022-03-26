from telnetlib import STATUS
from tkinter import CASCADE
from xml.dom.minidom import CharacterData
from django.db import models
from django.forms import CharField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length= 500)
    
    def __str__(self):
        return self.title
    
class Book(models.Model):
    title = models.CharField(max_length=2000)
    category = models.ForeignKey(Category,on_delete=models.CASCADE ,related_name='books')
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['date_created']
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=1000)
    category = models.ForeignKey(Category,on_delete=models.CASCADE ,related_name='products')
    price = models.IntegerField()
    stock = models.IntegerField()
    image_url = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['date_created']
    
    def __str__(self):
        return self.name