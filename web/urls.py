"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from PIL import Image
from django.contrib import admin
from django.urls import path, include
from home.views import indexh
from home.views import products
from home.views import product_detail
from home.views import cart
from home.views import account
from home.views import home_view
from home.views import userpanel
from home.views import productdetail1
from home.views import productdetail2
from home.views import about
from home.views import news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('product-detail.html/', product_detail),
    path('productdetail1.html/', productdetail1),
    path('productdetail2.html/', productdetail2),
    path('cart.html/', cart),
    path('account.html/', account),
    path('index.html/', indexh),
    path('account.html/index.html/', indexh),
    path('cart.html/index.html/', indexh),
    path('products.html/index.html/', indexh),
    path('index.html/products.html/', products),
    path('products.html/', products),
    path('post/', include('post.urls')),
    path('products.html/product-detail.html/', product_detail),
    path('account.html/userpanel.html/', userpanel),
    path('about.html/', about),
    path('news.html/', news),
    path('about.html/index.html/', indexh),
    path('news.html/index.html/', indexh),
    path('products.html/productdetail1.html/', productdetail1),
    path('products.html/productdetail2.html/', productdetail2),

]
