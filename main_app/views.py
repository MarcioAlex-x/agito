from django.shortcuts import render, get_object_or_404
from  .models import Post, Categoria
from django.utils import timezone
from django.core.paginator import Paginator


def index(request):
    search = request.GET.get('search')
    if search:
        posts = Post.objects.filter(titulo__icontains=search)
        categorias = Categoria.objects.all()
        # Fazer uma busca aqui
        # Instancia do Paginator com os valores enviados ao template
        posts_paginator = Paginator(posts, 5)
        # Definição da numeração da página
        page_num = request.GET.get('page')
        # Instancia da página
        page = posts_paginator.get_page(page_num)
        return render(request, 'main_app/index.html', {'page': page, 'posts':posts, 'categorias':categorias})
    else:
        posts = Post.objects.order_by('-published_date').all()
        categorias = Categoria.objects.all()
        # Fazer uma busca aqui
        # Instancia do Paginator com os valores enviados ao template
        posts_paginator = Paginator(posts, 5)
        # Definição da numeração da página
        page_num = request.GET.get('page')
        # Instancia da página
        page = posts_paginator.get_page(page_num)
        return render(request, 'main_app/index.html', {'page': page, 'posts':posts, 'categorias':categorias})

def detalhes_post(request, id):
    post = get_object_or_404(Post, id=id)
    categorias = Categoria.objects.all()
    return render(request, 'main_app/detalhes_post.html', {'post': post, 'categorias':categorias })
