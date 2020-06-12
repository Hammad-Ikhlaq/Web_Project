from django.contrib import admin

# Register your models here.
from .models import Cart, Products, Post

admin.site.register(Cart)
admin.site.register(Products)
admin.site.register(Post)