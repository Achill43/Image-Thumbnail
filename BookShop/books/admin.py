from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    """Display Category book in admin panel"""
    list_display = ['name', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        models = Category


class GenreAdmin(admin.ModelAdmin):
    """Display Genre book in admin panel"""
    list_display = ['name', 'parent', 'created_at']
    search_fields = ['name',  'description']
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        models = Genre


class AuthorAdmin(admin.ModelAdmin):
    """Display Auther of book in admin panel"""
    list_display = ['name', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        models = Author


class PublisherAdmin(admin.ModelAdmin):
    """Display Publisher of book in admin panel"""
    list_display = ['name', 'created_at']
    search_fields = ['name', 'address']
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        models = Publisher


class BookAdmin(admin.ModelAdmin):
    """Display Book in admin panel"""
    list_display = ['name', 'price', 'genre', 'created_at']
    search_fields = ['name', 'description', 'author', 'genre']
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        models = Book


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
