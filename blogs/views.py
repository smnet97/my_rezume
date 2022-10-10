from django.shortcuts import render
from .models import BlogModel
from django.views.generic import ListView
class BlogModelView(ListView):
    model = BlogModel
    template_name = 'blog.html'
