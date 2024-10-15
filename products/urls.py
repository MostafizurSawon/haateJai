from django.urls import path
from .views import Products
 
urlpatterns = [
    path('all/', Products, name='products'),
]
