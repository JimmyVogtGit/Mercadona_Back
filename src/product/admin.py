from django.contrib import admin
from .models import Category, Produit, Promotion

# Register your models here.

admin.site.register(Category)
admin.site.register(Produit)
admin.site.register(Promotion)
