from django.db import models
from django.utils import timezone


class Funcionario(models.Model):
    author = models.ForeignKey('auth.User')
    matricula = models.CharField(max_length=200)
    foto = models.ImageField(null=True, blank=True, upload_to='core')
    nome = models.CharField(max_length=70)    
    email = models.EmailField(max_length=70, blank=True)
    telefone = models.IntegerField()
    cargo = models.CharField(max_length=70)

    def publish(self):        
    	self.save()

    def __str__(self):
    	return self.nome


class Publicacao(models.Model):
	autor = models.ForeignKey(Funcionario)
	titulo = models.TextField()
	ano = models.DateField()
	arquivo = models.FileField(null=True, blank=True, upload_to='core/publicacao')

	def publish(self):
		self.save()

	def __str__(self):
		return self.titulo		

class Professor(models.Model):
	matricula = models.ForeignKey(Funcionario)
	slug = models.SlugField(max_length=70)
	regime_de_trabalho = models.CharField(max_length=12)
	lattes = models.CharField(null=True, blank=True, max_length=70)
	formacao = models.CharField(max_length=70)
	linha_de_pesquisa = models.TextField(null=True, blank=True)
	resumo = models.TextField(null=True, blank=True,)
	publicacoes = models.ManyToManyField(Publicacao, verbose_name="lista de publicacoes", blank=True)

	class Meta:
		ordering=['slug']

	def publish(self):
		self.save()

	def __str__(self):
		return self.matricula.nome
	    

class Tecnico_adm(models.Model):
	matricula = models.ForeignKey(Funcionario)
	slug = models.SlugField(max_length=70)

	def publish(self):
		self.save()

	def __str__(self):
		return self.matricula.nome


class Pesquisador(models.Model):
	matricula = models.ForeignKey(Funcionario)
	slug = models.SlugField(max_length=70)
	projeto = models.CharField(max_length=70)

	def publish(self):
		self.save()

	def __str__(self):
		return self.matricula.nome


class Bolsista(models.Model):
	matricula = models.ForeignKey(Funcionario)
	slug = models.SlugField(max_length=70)
	projeto = models.CharField(max_length=70)
	orientador = models.ForeignKey(Professor)

	def publish(self):
		self.save()

	def __str__(self):
		return self.matricula.nome


class Disciplina(models.Model):
	codigo = models.CharField(max_length=20)
	nome = models.CharField(max_length=70)
	slug = models.SlugField(max_length=70)
	arquivo = models.FileField(null=True, blank=True, upload_to='core/disciplinas')
	ano = models.DateField(null=True, blank=True)
	ementa = models.TextField(null=True, blank=True, max_length=500)		
	grau = models.CharField(max_length=20)

	class Meta:
		ordering=['slug']

	def publish(self):
		self.save()

	def __str__(self):
		return self.nome
	
class Laboratorio(models.Model):
	nome = models.CharField(max_length=70)
	slug = models.SlugField(max_length=70)
	descricao = models.TextField()
	link = models.CharField(null=True, blank=True, max_length=50)
	arquivo = models.FileField(null=True, blank=True, upload_to='core/documentos')

	def publish(self):
		self.save()

	def __str__(self):
		return self.nome

class Documento(models.Model):
	nome = models.CharField(max_length=70)
	slug = models.SlugField(max_length=70)
	link = models.CharField(null=True, blank=True, max_length=50)
	arquivo = models.FileField(null=True, blank=True, upload_to='core/documentos')

	def publish(self):
		self.save()

	def __str__(self):
		return self.nome

class Legislacao(models.Model):
	nome = models.CharField(max_length=70)
	slug = models.SlugField(max_length=70)
	link = models.CharField(null=True, blank=True, max_length=50)
	arquivo = models.FileField(null=True, blank=True, upload_to='core/documentos')

	def publish(self):
		self.save()

	def __str__(self):
		return self.nome


class Formulario(models.Model):
	nome = models.CharField(max_length=70)
	slug = models.SlugField(max_length=70)
	link = models.CharField(null=True, blank=True, max_length=50)
	arquivo = models.FileField(null=True, blank=True, upload_to='core/documentos')

	def publish(self):
		self.save()

	def __str__(self):
		return self.nome