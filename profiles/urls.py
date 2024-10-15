from django.urls import path
from .views import UserRegistrationView, UserLoginView, user_logout, active, profile
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('activate/<str:uid64>/<str:token>/', active, name = 'activate'),
]
