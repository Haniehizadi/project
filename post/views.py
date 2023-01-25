from django.shortcuts import render, HttpResponse
from .models import post

# Create your views here.

def index_view(request):
    posts = post.objects.all()
    return render(request, 'post/index.html', {"posts": posts})

def create_view(request):
    return HttpResponse("c")

def detail_view(request):
    post = post.object.get(id=3)
    return render(request, 'post/detail.html', {"posts": post})           

def update_view(request):
    return HttpResponse("u")

def delete_view(request):
    return HttpResponse("d")
