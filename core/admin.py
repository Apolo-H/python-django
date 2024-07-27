from django.contrib import admin
# admin.py

admin.site.site_header = "Meu Admin"
admin.site.site_title = "Título do Admin"
admin.site.index_title = "Bem-vindo ao Admin"

# Register your models here.
from .models import Product, Blog, Category,cafe
admin.site.register(Product)
admin.site.register(cafe)


#admin.site.register(Blog)
@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ['mini_image', 'blo_title']
    search_fields = ['blo_title']

class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"    

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['cat_name', 'slug']
    search_fields = ['cat_name']



