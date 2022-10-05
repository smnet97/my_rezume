from django.contrib import admin

from .models import BlogModel, CategoryModel


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['id', 'title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'body']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['id', 'name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
