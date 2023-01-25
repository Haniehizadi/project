from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    context = {'name':''}
    return render(request, 'index.html', context)

def indexh(request):
    context = {'name':''}
    return render(request, 'index.html', context)

def products(request):
    context = {'name':''}
    return render(request, 'products.html', context)        

def account(request):
    context = {'name':''}
    return render(request, 'account.html', context) 

def cart(request):
    context = {'name':''}
    return render(request, 'cart.html', context) 

def product_detail(request):
    context = {'name':''}
    return render(request, 'product-detail.html', context) 

def userpanel(request):
    context = {'name':''}
    return render(request, 'userpanel.html', context) 

def productdetail1(request):
    context = {'name':''}
    return render(request, 'productdetail1.html', context) 

def productdetail2(request):
    context = {'name':''}
    return render(request, 'productdetail2.html', context) 

def news(request):
    context = {'name':''}
    return render(request, 'news.html', context) 

def about(request):
    context = {'name':''}
    return render(request, 'about.html', context) 