from django.http import HttpResponseRedirect
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
from . models import CartItem, OrderItem, Orders, UserAccount, Cart
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
        confirm_link = f"https://haatejai.onrender.com/accounts/activate/{uid}/{token}/"
        # confirm_link = f"http://127.0.0.1:8000/user/activate/{uid}/{token}/"
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
    orders = Orders.objects.filter(user=request.user)

    # Pass the orders to the template
    context = {
        'orders': orders,
        'user_profile': user_profile
    }
    return render(request, 'profile.html', context)

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
    
    # Get the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the product exists in the cart
    cart_item = CartItem.objects.filter(cart=cart, product=product).first()

    if cart_item:
        # If the product is in the cart, remove the item
        cart_item.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

from .forms import AddressForm  # Assuming you have a form to handle address input

@login_required
def add_address(request):
    user_account = get_object_or_404(UserAccount, user=request.user)

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=user_account)
        if form.is_valid():
            form.save()
            return redirect('checkout')  # Redirect to the cart or any other page after saving
    else:
        form = AddressForm(instance=user_account)  # Load the current user's address if any

    return render(request, 'add_address.html', {'form': form})

# @login_required
# def update_cart_item_quantity(request, cart_item_id):
#     cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
#     print("foing1")
#     if request.method == 'POST':
#         action = request.POST.get('action')
#         print("foing2")
#         if action == 'increase':
#             print("foing")
#             cart_item.quantity += 1
#         elif action == 'decrease' and cart_item.quantity > 1:
#             cart_item.quantity -= 1
        
#         cart_item.save()
    
#     return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def place_order(request):
    # Fetch the user's active cart
    cart = get_object_or_404(Cart, user=request.user, complete=False)
    
    # Calculate the total amount from cart items
    total_amount = sum(item.product.price * item.quantity for item in cart.items.all())

    # Create the order with the total amount
    order = Orders.objects.create(user=request.user, total_amount=total_amount)

    # Create OrderItems for each item in the cart
    for item in cart.items.all():
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)

    # Clear the cart items
    cart.items.all().delete()
    cart.save()

    # Redirect to a confirmation page or wherever you want
    return redirect('profile')

from .models import Orders, OrderItem



@login_required
def order_details(request, order_id):
    order = get_object_or_404(Orders, id=order_id, user=request.user)  # Ensure the order belongs to the logged-in user
    order_items = order.order_items.all()  # Use the related name to get order items

    context = {
        'order': order,
        'items': order_items,
    }
    return render(request, 'order_details.html', context)

