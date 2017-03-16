from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from .models import  Funcionario, Professor, Documento, Disciplina, Formulario, Legislacao, Laboratorio, Evento, Especializacao
from noticia.models import Post

def index(request):	
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    primeira = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:1]
    segunda = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[1:2]    
    janeiro = Evento.objects.filter(data__month=1).order_by('-data')
    fevereiro = Evento.objects.filter(data__month=2).order_by('-data')
    marco = Evento.objects.filter(data__month=3).order_by('-data')
    abril = Evento.objects.filter(data__month=4).order_by('-data')
    maio = Evento.objects.filter(data__month=5).order_by('-data')
    junho = Evento.objects.filter(data__month=6).order_by('-data')
    julho = Evento.objects.filter(data__month=7).order_by('-data')
    agosto = Evento.objects.filter(data__month=8).order_by('-data')
    setembro = Evento.objects.filter(data__month=9).order_by('-data')
    outubro = Evento.objects.filter(data__month=10).order_by('-data')
    novembro = Evento.objects.filter(data__month=11).order_by('-data')
    dezembro = Evento.objects.filter(data__month=12).order_by('-data')
    painel1 = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:4]
    painel2 = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[4:8]    
    template = 'core/index.html'
    context = {
        'posts': posts,
        'primeira': primeira,
        'segunda': segunda,        
        'painel1': painel1,
        'painel2': painel2,
        'janeiro': janeiro,
        'fevereiro': fevereiro,
        'marco': marco,
        'abril': abril,
        'maio': maio,
        'junho': junho,
        'julho': julho,
        'agosto': agosto,
        'setembro': setembro,
        'outubro': outubro,
        'novembro': novembro,
        'dezembro': dezembro
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

def lista_especializacoes(request):
    especializacoes = Especializacao.objects.all()
    template = 'core/especializacoes.html'
    context = {
            'especializacoes': especializacoes
    }
    return render(request, template, context)

def especializacao_detail(request, slug):
    especializacao = get_object_or_404(Especializacao, slug=slug)
    template = 'core/especializacao.html'
    context = {
        'especializacao': especializacao
    }
    return render(request, template, context)

def lista_administrativo(request):
    chefia = Funcionario.objects.filter(Q(cargo ='Chefe') | Q(cargo ='Vice-Chefe'))
    secretarios = Funcionario.objects.filter(cargo='secretaria')
    template = 'core/administrativo.html'
    context = {
            'chefia': chefia,
            'secretarios': secretarios
    }
    return render(request, template, context)


