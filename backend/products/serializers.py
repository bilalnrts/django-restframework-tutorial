from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField()
    my_raise = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'my_raise'
        ]
    
    def get_my_discount(self, obj):
        return obj.get_discount()
    
    def get_my_raise(self, obj):
        return float(obj.price) * 1.2
