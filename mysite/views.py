from django.shortcuts import render
from rest_framework import generics
from .serializer import *
# Create your views here.

class ListCategory(generics.ListAPIView):
    query_set = Category.objects.all()
    serializer_class = CategorySerializer
    
class DetailsCategory(generics.RetrieveUpdateDestroyAPIView):
    query_set = Category.objects.all()
    serializer_class = CategorySerializer
    
class ListBook(generics.ListAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer

class DetailsBook(generics.RetrieveUpdateDestroyAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer
    
class ListProduct(generics.ListAPIView):
    query_set = Product.objects.all()
    serializer_class = ProductSerializer
    
class DetailsProduct(generics.RetrieveUpdateDestroyAPIView):
    query_set = Product.objects.all()
    serializer_class = ProductSerializer
    
