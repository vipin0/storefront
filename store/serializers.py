from decimal import Decimal
from rest_framework import serializers
from .models import Collection, Product, Review

TAX_PERCENT = 1.1

class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ['id','title','products_count']
    
    products_count = serializers.IntegerField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','title','description','slug','unit_price','price_with_tax','inventory','collection']

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return round(product.unit_price * Decimal(TAX_PERCENT),2)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id','date','name','description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id,**validated_data )
