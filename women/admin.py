from django.contrib import admin

# Register your models here.

from .models import Women, Category


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'cat')
    list_editable = ('is_published', )
    list_display_links = ('title', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
