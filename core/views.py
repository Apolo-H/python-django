from django.shortcuts import render
from core.models import Product


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
        'products': product,
    }
    return render(request, 'produtos.html', data)

def about (request):
        context = {
        'courses': 'Programação de Computadores no SENAC GUA',
        'languages': ['Python', 'Java', 'C#', 'JavaScript'],
    }
        return render(request, 'about.html', context)	

