from django.contrib import admin
from PIL import Image
 #Register your models here.
from .models import post

class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'published_date']
    list_display_links = ['title', 'published_date']
    list_filter = ['published_date']
    search_fields = ['title', 'content']
    images = ['image', 'image']

    class Meta:
        model = post

admin.site.register(post, PostAdmin)

