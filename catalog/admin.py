from django.contrib import admin

# Register your models here.
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin): #Model que vai modificar o admin
    list_display = ['name', 'slug','created', 'modified'] #lista os campos que serão mostrados no admin
    search_fields = ['name', 'slug'] #os campos de pesquisa
    list_filter = ['created', 'modified']# filtros de pesquisa

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','category','created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']

admin.site.register(Product,ProductAdmin) # registrando os models e modelsAdmin no django Admin
admin.site.register(Category, CategoryAdmin)