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
    vegs =[]
    meats =[]
    fishes =[]
    fruits =[]
    types =[]
    offers =[]
    for product in products:
        if any(cat.name.lower() == 'vegetables' for cat in product.category.all()):
            # print("1Yes, this product is a vegetable")
            vegs.append(product)
        
    for product in products:
        if any(cat.name.lower() == 'meat' for cat in product.category.all()):
            # print("1Yes, this product is a vegetable")
            meats.append(product)
            
    for product in products:
        if any(cat.name.lower() == 'fish' for cat in product.category.all()):
            # print("1Yes, this product is a vegetable")
            fishes.append(product)
            
    for product in products:   
        if any(cat.name.lower() == 'fruits' for cat in product.category.all()):
            # print("1Yes, this product is a vegetable")
            fruits.append(product)
            
    for product in products:   
        if any(cat.name.lower() == 'hot' for cat in product.type.all()):
            # print("1Yes, this product is a vegetable")
            types.append(product)
            
    for product in products:   
        if any(cat.name.lower() == 'offer' for cat in product.type.all()):
            # print("1Yes, this product is a vegetable")
            offers.append(product)
        

    # for product in products:
    #     # Check if any category's name is 'vegetables' (case insensitive)
    #     if any(cat.name.lower() == 'vegetables' for cat in product.category.all()) and any(loc.name.lower() == 'uttara' for loc in product.location.all()):
    #         print("1Yes, this product is a vegetable")
    #     else:
    #         print("No vegetables in this product")

    # cart_items = []

    # if request.user.is_authenticated:
    #     # Get the active cart for the authenticated user
    #     cart = Cart.objects.filter(user=request.user, complete=False).first()
    #     if cart:
    #         cart_items = cart.items.all()  # Retrieve all items from the cart
    # print('cart ->',cart)
    # print('cart items ->',cart_items)
    # print(vegs)
    context = {
        'products': products,
        'vegs': vegs,
        'meats': meats,
        'fishes': fishes,
        'fruits': fruits,
        'types': types,
        'offers': offers,
    }
    # print(context)
    return render(request, 'base.html', context)

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