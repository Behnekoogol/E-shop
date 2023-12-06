from django.contrib import admin
from .models import Category, Product, ProductImage, Gender



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'active')


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ['gender']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    prepopulated_fields = prepopulated_fields = {'slug': ('name', )}



@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image', )

