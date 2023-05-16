from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.static import serve
from django.urls import re_path
from . import views
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
public_html_dir = os.path.abspath(os.path.join(current_dir, '../../../../public_html'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('', include('authenticate.urls')),
    path('', include('product.urls')),
    re_path(r'^.*$', serve, {'document_root': public_html_dir})

]
