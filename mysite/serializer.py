from .models import *
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title','category','isbn','price','pages','stock','description','image_url','status','date_created')

    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title')
        model = Category
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','product_tag','name','category','price','stock','image_url','status','date_created')
        model = Book
        