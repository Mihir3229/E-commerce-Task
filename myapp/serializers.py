from rest_framework import serializers
from .models import Customer, Product, Order, OrderItem
from datetime import date

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'contact_number', 'email']
        
    def validate_name(self, value):
        existing_customers = Customer.objects.filter(name=value)
        if self.instance:
            existing_customers = existing_customers.exclude(pk=self.instance.pk)
        if existing_customers.exists():
            raise serializers.ValidationError("Customer's name must be unique.")
        return value

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'weight']
        
    def validate_name(self, value):
        existing_products = Product.objects.filter(name=value)
        if self.instance:
            existing_products = existing_products.exclude(pk=self.instance.pk)
        if existing_products.exists():
            raise serializers.ValidationError("Product's name must be unique.")
        return value

    def validate_weight(self, value):
        if value <= 0 or value > 25:
            raise serializers.ValidationError("Weight must be a positive decimal and not more than 25kg.")
        return value

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'order_number', 'customer', 'order_date', 'address', 'order_items']
    
    def validate_order_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Order Date cannot be in the past.")
        return value

    def validate(self, data):
        order_items_data = data.get('order_item')
        total_weight = sum(item['product'].weight * item['quantity'] for item in order_items_data)
        if total_weight > 150:
            raise serializers.ValidationError("Order cumulative weight must be under 150kg.")
        return data
