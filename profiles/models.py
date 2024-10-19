from django.db import models
from django.contrib.auth.models import User
import random
from products.models import Products

class UserAccount(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    TYPE_CHOICES = [
        ('Super', 'Super'),
        ('Regular', 'Regular'),
        ('Below Average', 'Below Average'),
    ]
    
    LOCATION_CHOICES = [
        ('Uttara', 'UTTARA'),
        ('Mirpur', 'MIRPUR'),
        ('Dhanmondi', 'DHANMONDI'),
    ]

    images = [
        'https://img.freepik.com/free-photo/androgynous-avatar-non-binary-queer-person_23-2151100207.jpg',
        'https://img.freepik.com/free-photo/cartoon-character-with-handbag-sunglasses_71767-99.jpg',
        'https://img.freepik.com/free-photo/anime-style-character-space_23-2151134190.jpg',
        'https://img.freepik.com/premium-photo/poster-anime-character-with-fiery-background_943629-32000.jpg',
        'https://img.freepik.com/free-photo/androgynous-avatar-non-binary-queer-person_23-2151100183.jpg'
    ]

    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, blank=True, choices=TYPE_CHOICES, default="Regular")
    verify = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True, null=True, blank=True)
    image = models.URLField(blank=True, null=True, default=random.choice(images))
    gender = models.CharField(max_length=20, blank=True, choices=GENDER_CHOICES)
    mobile = models.CharField(max_length=14, blank=True)
    points = models.IntegerField(null=True, blank=True, default=0)
    age = models.IntegerField(null=True, blank=True)
    hometown = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    current_location = models.CharField(max_length=20, blank=True, choices=LOCATION_CHOICES, default="UTTARA")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.user.first_name


class UserSocialAccount(models.Model):
    facebook = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    x = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    user = models.OneToOneField(User, related_name='social_account', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart_account', on_delete=models.CASCADE)
    complete = models.BooleanField(default=False, blank=True)
    complete_date = models.DateTimeField(null=True, blank=True)
    pending_date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s cart."


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} in {self.cart.user.username}'s cart."


class Orders(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, related_name='order_account', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Orders, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Store the price of the product at the time of order

    def __str__(self):
        return f"{self.product.name} in Order {self.order.id}"
