from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

from products.models import Products
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

def home(request):
    products = Products.objects.all()
    print("hii",products)
    # if category_slug is not None:
    #     categories = Category.objects.get(slug = category_slug)
    #     jokes = Joke.objects.filter(categories  = categories)
    # categories = Category.objects.all()
    # h_joke = jokes.order_by('-like').first()
    # return render(request, 'home.html', {'jokes' : jokes, 'categories' : categories, 'hjoke' : h_joke})
    return render(request, 'base.html', {'products' : products, 'demo': 'yes got t'})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def filter_home(request, category):
    categories = Category.objects.all()
    category = get_object_or_404(Category, name=category)
    jokes = Joke.objects.filter(categories=category)
    
    return render(request, "home.html", {"jokes":jokes, "categories":categories})