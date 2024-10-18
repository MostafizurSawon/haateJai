from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

from products.models import Products
from profiles.models import Cart
# from jokes.models import Joke, Category


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['jokes'] = Joke.objects.all()
        context['categories'] = Category.objects.all()
        return context

# class HomeView(TemplateView):
#     template_name = 'home.html'
    
#     def get_context_data(self,*args, **kwargs):
#         context = super().get_context_data(*args,**kwargs)
#         context['books'] = Book.objects.all()
#         context['categories'] = Category.objects.all()
#         return context
    

# def home(request):
#     categories = Category.objects.all()
#     jokes = Joke.objects.all()
    
#     return render(request, "home.html", {"jokes":jokes, "categories":categories})

from django.conf import settings
from django.http import FileResponse, HttpResponse
import os

def download_database(request):
    db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')  # This will dynamically fetch the path
    if os.path.exists(db_path):
        response = FileResponse(open(db_path, 'rb'))
        return response
    else:
        return HttpResponse("Database not found.", status=404)

def home(request):
    products = Products.objects.all()
    # cart_items = []

    # if request.user.is_authenticated:
    #     # Get the active cart for the authenticated user
    #     cart = Cart.objects.filter(user=request.user, complete=False).first()
    #     if cart:
    #         cart_items = cart.items.all()  # Retrieve all items from the cart
    # print('cart ->',cart)
    # print('cart items ->',cart_items)
    
    return render(request, 'base.html', {'products': products})

# def home(request):
#     cart_products = Cart.objects.filter(user__user=request.user).prefetch_related('products').first()
    
#     return render(request, 'home.html', {'cart_products': cart_products})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


# def filter_home(request, category):
#     categories = Category.objects.all()
#     category = get_object_or_404(Category, name=category)
#     jokes = Joke.objects.filter(categories=category)
    
#     return render(request, "home.html", {"jokes":jokes, "categories":categories})