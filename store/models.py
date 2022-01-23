from uuid import uuid4
from django.core.validators import MinValueValidator
from django.conf import settings
from django.db import models


# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20,null=True,blank=True)
    birth_date = models.DateField(null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='addresses')


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2,validators=[MinValueValidator(0)])
    inventory = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT,related_name='product')
    promotions = models.ManyToManyField(Promotion,related_name='product',blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
        
class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED,'Failed'),
    ]
    payment_status = models.CharField(
                            max_length=1,
                            choices=PAYMENT_STATUS_CHOICES,
                            default=PAYMENT_STATUS_PENDING
                    )
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT,related_name='order')
    placed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ('cancel_order','Can cancel order')
        ]

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT,related_name='order_item')
    product = models.ForeignKey(Product,on_delete=models.PROTECT,related_name='order_item')
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)

class Cart(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    created_on = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        unique_together = [['cart','product']]

class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="reviews")
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
