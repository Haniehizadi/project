from django.shortcuts import render,  HttpResponse

# Create your views here.

def about_page(request):
    context = {'name':''}
    return render(request, 'product-detail.html', context)