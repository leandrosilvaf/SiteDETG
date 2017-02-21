from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import  Funcionario, Professor, Documento, Disciplina, Formulario, Legislacao, Laboratorio, Evento
from noticia.models import Post, Principal

def index(request):	
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    primeira = Principal.objects.get(pk=1)
    segunda = Principal.objects.get(pk=2)
    terceira = Principal.objects.get(pk=3)
    janeiro = Evento.objects.filter(data__month=1).order_by('-data')
    fevereiro = Evento.objects.filter(data__month=2).order_by('-data')
    marco = Evento.objects.filter(data__month=3).order_by('-data')
    painel1 = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:4]
    painel2 = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[4:8]    
    template = 'core/index.html'
    context = {
        'posts': posts,
        'primeira': primeira,
        'segunda': segunda,
        'terceira': terceira,
        'painel1': painel1,
        'painel2': painel2,
        'janeiro': janeiro,
        'fevereiro': fevereiro,
        'marco': marco
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
    documentos = Documento.objects.all()
    template = 'core/base.html'
    context = {
            'documentos': documentos
    }
    return render(request, template, context)

def lista_legislacoes(request):
    legislacoes = Documento.objects.all()
    template = 'core/base.html'
    context = {
            'legislacoes': legislacoes
    }
    return render(request, template, context)

def lista_formularios(request):
    formularios = Documento.objects.all()
    template = 'core/base.html'
    context = {
            'formularios': formularios
    }
    return render(request, template, context)

def lista_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    template = 'core/laboratorios.html'
    context = {
            'laboratorios': laboratorios
    }
    return render(request, template, context)

def laboratorio_detail(request, slug):
    laboratorio = get_object_or_404(Laboratorio, slug=slug)
    template = 'core/laboratorio.html'
    context = {
        'laboratorio': laboratorio
    }
    return render(request, template, context)


