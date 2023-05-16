from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.static import serve
from django.urls import re_path
from . import views
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('', include('authenticate.urls')),
    path('', include('product.urls')),

]
