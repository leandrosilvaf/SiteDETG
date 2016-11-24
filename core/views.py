from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import  Funcionario, Professor, Documento, Disciplina, Formulario, Legislacao
from noticia.models import Post, Principal

def index(request):	
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    primeira = Principal.objects.get(pk=1)
    segunda = Principal.objects.get(pk=2)
    terceira = Principal.objects.get(pk=3)
    painel1 = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:4]
    painel2 = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[4:8]    
    template = 'core/index.html'
    context = {
        'posts': posts,
        'primeira': primeira,
        'segunda': segunda,
        'terceira': terceira,
        'painel1': painel1,
        'painel2': painel2
    }   
    return render(request, template, context)

def lista_docentes(request):
    docentes = Professor.objects.all()
    template = 'core/docentes.html'
    context = {
            'docentes': docentes
    }
    return render(request, template, context)

def docente_detail(request, slug):
    docente = get_object_or_404(Professor, slug=slug)
    template = 'core/docente.html'
    context = {
        'docente': docente
    }
    return render(request, template, context)

def lista_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    template = 'core/graduacao.html'
    context = {
            'disciplinas': disciplinas
    }
    return render(request, template, context)

def lista_documentos(request):
    documentos = Documentos.objects.all()
    template = 'core/base.html'
    context = {
            'documentos': documentos
    }
    return render(request, template, context)

def lista_legislacoes(request):
    legislacoes = Documentos.objects.all()
    template = 'core/base.html'
    context = {
            'legislacoes': legislacoes
    }
    return render(request, template, context)

def lista_formularios(request):
    formularios = Documentos.objects.all()
    template = 'core/base.html'
    context = {
            'formularios': formularios
    }
    return render(request, template, context)




    
