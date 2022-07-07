from rest_framework import serializers
from django.contrib.auth.models import User

class ProductSerializer(serializers.Serializer):
 title = serializers.CharField(max_length = 100)
 Product_quantity = serializers.IntegerField(default = 0)
 selling_price = serializers.FloatField()
 discounted_price = serializers.FloatField()
 description = serializers.CharField()
 brand = serializers.CharField( max_length = 100)
 category = serializers.CharField(  max_length = 2)
 product_image = serializers.ImageField()


