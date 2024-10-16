from django.urls import path
from .views import UserRegistrationView, UserLoginView, user_logout, active, profile, add_to_cart, remove_from_cart, checkout
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('activate/<str:uid64>/<str:token>/', active, name = 'activate'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('checkout/', checkout, name='checkout'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]
