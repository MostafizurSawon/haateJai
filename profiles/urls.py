from django.urls import path
from .views import UserRegistrationView, UserLoginView, user_logout, active, profile, add_to_cart, remove_from_cart, checkout, add_address, place_order,order_details
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('activate/<str:uid64>/<str:token>/', active, name = 'activate'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    # path('profile/', user_orders, name='user_orders'),
    path('profile/', profile, name='profile'),
    path('checkout/', checkout, name='checkout'),
    path('add-address/', add_address, name='add_address'),
    path('place-order/', place_order, name='place_order'),
     path('orders/<int:order_id>/', order_details, name='user_order_details'),
    # path('update-cart-item/<int:cart_item_id>/', update_cart_item_quantity, name='update_cart_item_quantity'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]
