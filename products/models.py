from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=50)
  delete = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  
  def __str__(self):
    return self.name

class Products(models.Model):
  TYPE_CHOICES = [
      ('Hot', 'Hot'),
      ('New', 'New'),
      ('Offer', 'Offer'),
  ]
  
  name = models.CharField(max_length=100)
  image = models.URLField(blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  type = models.CharField(max_length=20, blank=True, choices=TYPE_CHOICES)
  quantity = models.IntegerField(blank=True, null=True)
  price = models.IntegerField(blank=True, null=True)
  discount_price = models.IntegerField(blank=True, null=True)
  category = models.ForeignKey(Category, related_name='product_category', on_delete=models.CASCADE)
  sold = models.IntegerField(blank=True, null=True, default=0)
  available = models.IntegerField(blank=True, null=True)
  delete = models.BooleanField(default=False)
  user = models.ForeignKey(User, related_name='product_owner', on_delete=models.CASCADE,default=1)
  created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  
  def __str__(self):
    return f"{self.name} by {self.user.username}"
  