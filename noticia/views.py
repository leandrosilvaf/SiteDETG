from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Principal


def noticias(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    primeira = Principal.objects.get(pk=1)
    segunda = Principal.objects.get(pk=2)
    terceira = Principal.objects.get(pk=3)
    return render(request, 'noticia/noticias.html', {'posts': posts, 'primeira': primeira, 'segunda': segunda, 'terceira': terceira})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'noticia/post_detail.html', {'post': post})

