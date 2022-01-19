from django.contrib import admin
from .models import Order, Product, Post, Category

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Post)
admin.site.register(Category)
