from django.views.generic import FormView
from django.shortcuts import redirect,get_object_or_404, render
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
# from jokes.models import Joke
from . models import CartItem, UserAccount, Cart
from products.models import Products

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User


class UserRegistrationView(FormView):
    template_name = 'user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()

        token = default_token_generator.make_token(user)
        print("token ", token)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        print("uid ", uid)

        # sometimes working sometimes not working the verification email link
        confirm_link = f"http://127.0.0.1:8000/user/activate/{uid}/{token}/"
        email_subject = "Confirm Your Email"
        email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
        email = EmailMultiAlternatives(email_subject , '', to=[user.email])
        email.attach_alternative(email_body, "text/html")
        email.send()
        # print(confirm_link)
        return super().form_valid(form)

def active(request, uid64, token):
    # print("I am in")
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        # print("token ->",token)
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        # print(token)
        return redirect('register')
    
    
class UserLoginView(LoginView):
    template_name = 'user_login.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('profile'))
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('profile')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


# class ProfileView(TemplateView):
#     template_name = 'profile.html'
    
#     def get_context_data(self,*args, **kwargs):
#         context = super().get_context_data(*args,**kwargs)
#         context['jokes'] = Joke.objects.all()
#         # context['categories'] = Category.objects.all()
#         return context

@login_required(login_url=reverse_lazy('login'))
def profile(request):
    user = request.user
    # user_profile = UserAccount.objects.filter(user=user).first()
    user_profile = UserAccount.objects.filter(user=user)
    # print(user_profile.points)
    return render(request, 'profile.html', {'user_profile': user_profile})

@login_required(login_url=reverse_lazy('login'))
def checkout(request):
    return render(request, 'cart.html')



from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from products.models import Products
from .models import Cart

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    quantity = int(request.POST.get('quantity', 1))  # Get quantity from POST data

    # Get or create an active cart for the user
    cart, created = Cart.objects.get_or_create(user=request.user, complete=False)

    # Check if the product is already in the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if item_created:
        # If it's a new item, set the initial quantity
        cart_item.quantity = quantity
    else:
        # If the item already exists, update its quantity
        cart_item.quantity += quantity

    # Save the cart item
    cart_item.save()

    return redirect('home')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    user_account = UserAccount.objects.get(user=request.user)
    
    cart, created = Cart.objects.get_or_create(user=user_account)
    
    if cart.products.filter(id=product.id).exists():
        cart.products.remove(product)
    
    return redirect('checkout')

