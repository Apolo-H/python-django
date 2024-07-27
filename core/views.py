from django.shortcuts import render
from core.models import Product, Blog
from django.shortcuts import render, get_object_or_404

def index (request):
    data = {
        'title': 'Venha conhecer Nossa cafeteria: Onde Cada Xícara Conta uma História Miauravilhosa',
        'languages': ['Python', 'Java', 'C#', 'JavaScript'],
        'news': [
            {
                'title': 'Nova versão do Django lançada!',
                'subtitle': 'Confira as novidades da versão 3.0',
                'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis libero ut imperdiet vehicula.'
            },
            {
                'title': 'Python é a linguagem do futuro',
                'subtitle': 'Especialistas afirmam que Python está dominando o mercado',
                'text': 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
            },
            {
                'title': 'JavaScript: O que esperar do ES10?',
                'subtitle': 'Novas funcionalidades e melhorias na performance',
                'text': 'Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.'
            }
        ]
    }
    
    return render(request, 'index.html', data)

def product (request):
    product = Product.objects.all()

    data = {
        'product': product,
    }
    
    return render(request, 'produtos.html', data)

def produto_single(request, id):
    product = get_object_or_404(Product, id=id), # get_object_or_404(Products, id=id) -> Usado para recuperar um único objeto com base em um critério específico, como um ID único.
    return render(request, 'produto_single.html', {'product': product}) 


def about (request):
        context = {
        'courses': 'Programação de Computadores no SENAC GUA',
        'languages': ['Python', 'Java', 'C#', 'JavaScript'],
    }
        return render(request, 'about.html', context)	


def blog (request):
    blog = Blog.objects.all()

    data = {
        'blog': blog,
        'title': 'Blog Django'
    }
    
    return render(request, 'blog.html', data)	

def blog_single(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_single.html', {'blog': blog})

def cafe(request, slug):
    cafe = get_object_or_404(Blog, slug=slug)
    return render(request, 'forms.html', {'cafe': cafe})

