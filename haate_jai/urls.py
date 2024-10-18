"""
URL configuration for haate_jai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . views import home, download_database

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', HomeView.as_view(), name="home"),
    path('', home, name="home"),
    path('down/', download_database, name="sqldata"),
    # path('category/<slug:category_slug>/', home, name="filter"),
    path('user/', include("profiles.urls")),
    path('products/', include("products.urls")),
    # path('reviews/', include("reviews.urls")),
    # path('about-us/', about, name="about"),
    # path('contact-us/', contact, name="contact"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
