from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def noticias(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')    
    return render(request, 'noticia/noticias.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'noticia/post_detail.html', {'post': post})

