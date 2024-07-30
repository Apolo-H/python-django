from django.db import models
from django.utils.text import slugify
from django.utils.html import format_html


class Blog(models.Model):
    blo_title = models.CharField('Título', max_length=100)
    blo_subtitle = models.CharField('Sub-Título', max_length=100, blank=True, null=True)
    blo_description = models.TextField('Texto do Blog')
    #blo_description = HTMLField('Texto do Blog')
    blo_image = models.ImageField('Imagem de Capa', upload_to='images/blog', blank=True, null=True)
    # image = models.ImageField(upload_to='images/', default='images/default.jpg')
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    #Abaixo o slug possui a função de adicionar um sufixo caso já exista com o mesmo nome
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.blo_title)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    #mini_image para retornar a imagem em miniatura no painel admin
    def mini_image(self):
        if self.blo_image:
            return format_html('<img src="{}" style="height: 100px; width: auto;" />', self.blo_image.url)
        return " "
    mini_image.short_description = 'Imagem de Capa'

    #A função abaixo é para retornar o name do produto na exibição dentro do painel admin
    def __str__(self):
       return self.blo_title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"



    
class Category(models.Model):
    cat_name = models.CharField('Nome da Categoria', unique=True, max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    #Criação do slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.cat_name)
        super().save(*args, **kwargs)
    
    #Abaixo o slug possui a função de adicionar um sufixo caso já exista com o mesmo nome
    #A função abaixo é para retornar o name do produto na exibição dentro do painel admin
    def __str__(self):
        return self.cat_name

class Product (models.Model):
    name = models.CharField('Nome', max_length=100)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    stock = models.IntegerField('Quantidade em Estoque')
    pro_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField('Imagem de Capa', upload_to='images/produto', blank=True, null=True)

    def __str__(self):
        return self.name
    

class cafe (models.Model):
    caf_name = models.CharField('Nome', max_length=100)
    caf_price = models.DecimalField('preço', decimal_places=2, max_digits=8)
    caf_estoque =  models.IntegerField('Quantidade em Estoque')
    caf_category =  models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    caf_image = models.ImageField('Imagem de Capa', upload_to='images/cafes', blank=True, null=True)

    def __str__(self):
        return self.caf_name
    
    



class CategoryTecnology(models.Model):
    cattec_name = models.CharField('Nome da Categoria da Tecnologia', max_length=100, unique=True) # a chave "unique=True" não permitirá cadastrar 2 valores iguais

    def __str__(self):
        return self.cattec_name

    class Meta:
        verbose_name = "Categoria da Tecnologia"
        verbose_name_plural = "Categorias das Tecnologias"


class Tecnology(models.Model):
    tec_name = models.CharField('Nome', max_length=100)
    tec_description = models.TextField('Texto do Tecnologia')
    #tec_description = HTMLField('Texto do Blog')
    tec_image = models.ImageField('Imagem de Capa', upload_to='images/tecnologia', blank=True, null=True)
    # image = models.ImageField(upload_to='images/', default='images/default.jpg')
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    tec_category = models.ForeignKey(CategoryTecnology, on_delete=models.CASCADE, null=True)
    
    #Abaixo o slug possui a função de adicionar um sufixo caso já exista com o mesmo nome
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.tec_name)
            slug = base_slug
            counter = 1
            while Tecnology.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    #mini_image para retornar a imagem em miniatura no painel admin
    def mini_image(self):
        if self.tec_image:
            return format_html('<img src="{}" style="height: 100px; width: auto;" />', self.tec_image.url)
        return " "
    mini_image.short_description = 'Imagem de Capa'

    #A função abaixo é para retornar o name do produto na exibição dentro do painel admin
    def __str__(self):
       return self.tec_name

    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"