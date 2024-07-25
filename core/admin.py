from django.contrib import admin
# admin.py

from django.contrib import admin
admin.site.site_header = "Meu Admin"
admin.site.site_title = "Título do Admin"
admin.site.index_title = "Bem-vindo ao Admin"

# Register your models here.
from .models import Product, Blog, Category
admin.site.register(Product)

#admin.site.register(Blog)
@admin.register(Blog)
class Blog(admin.ModelAdmin):
    #form = BlogAdminForm # Estilização do Form Blog do Admin
    list_display = ['mini_image', 'blo_title']
    search_fields = ['blo_title']


def __str__(self):
        return self.cat_name

class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"    

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['cat_name', 'slug']
    search_fields = ['cat_name']






