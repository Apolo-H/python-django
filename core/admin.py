from django.contrib import admin
# admin.py

admin.site.site_header = "Meu Admin"
admin.site.site_title = "Título do Admin"
admin.site.index_title = "Bem-vindo ao Admin"

# Register your models here.
from .models import Product, Blog, Category,cafe, CategoryTecnology, Tecnology
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




@admin.register(CategoryTecnology)
class CategoryTecnology(admin.ModelAdmin):
    list_display = ['cattec_name']
    search_fields = ['cattec_name']

@admin.register(Tecnology)
class Tecnology(admin.ModelAdmin):
    list_display = ['tec_name', 'mini_image']
    search_fields = ['tec_name']