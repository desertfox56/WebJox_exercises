from rest_framework import serializers
from .models import Product, Store

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'quantity', 'image', 'image']

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model= Store
        fields = ['id', 'name', 'description']