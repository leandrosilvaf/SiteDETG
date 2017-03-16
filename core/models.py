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
	nome = models.CharField(max_length=150)
	slug = models.SlugField(max_length=70)
	imagens = models.ImageField(null=True, blank=True, upload_to='core/laboratorio')
	descricao = models.TextField()
	hardware = models.TextField(null=True, blank=True, max_length=300)
	software = models.TextField(null=True, blank=True, max_length=300)
	agenda = models.CharField(null=True, blank=True, max_length=70)

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


class Evento(models.Model):
	nome = models.CharField(max_length=100)	
	data = models.DateField(null=True, blank=True)
	arquivo = models.FileField(null=True, blank=True, upload_to='core/documentos')

	def publish(self):
		self.save()

	def __str__(self):
		return self.nome

class Especializacao(models.Model):
	nome = models.CharField(max_length=150)
	slug = models.SlugField(max_length=70)
	imagens = models.ImageField(null=True, blank=True, upload_to='core/especializacao')	
	titulo1 = models.CharField(max_length=150)
	descricao1 = models.TextField(null=True, blank=True)
	titulo2 = models.CharField(null=True, blank=True, max_length=150)
	item21 = models.CharField(null=True, blank=True, max_length=150)
	item22 = models.CharField(null=True, blank=True, max_length=150)
	item23 = models.CharField(null=True, blank=True, max_length=150)
	item24 = models.CharField(null=True, blank=True, max_length=150)
	item25 = models.CharField(null=True, blank=True, max_length=150)
	item26 = models.CharField(null=True, blank=True, max_length=150)
	item27 = models.CharField(null=True, blank=True, max_length=150)
	item28 = models.CharField(null=True, blank=True, max_length=150)
	item29 = models.CharField(null=True, blank=True, max_length=150)
	item210 = models.CharField(null=True, blank=True, max_length=150)
	item211= models.CharField(null=True, blank=True, max_length=150)
	item212 = models.CharField(null=True, blank=True, max_length=150)	
	titulo3 = models.CharField(null=True, blank=True, max_length=150)
	descricao3 = models.TextField(null=True, blank=True)
	titulo4 = models.CharField(null=True, blank=True, max_length=150)
	item41 = models.CharField(null=True, blank=True, max_length=150)
	item42 = models.CharField(null=True, blank=True, max_length=150)
	item43 = models.CharField(null=True, blank=True, max_length=150)
	item44 = models.CharField(null=True, blank=True, max_length=150)
	item45 = models.CharField(null=True, blank=True, max_length=150)
	item46 = models.CharField(null=True, blank=True, max_length=150)
	item47 = models.CharField(null=True, blank=True, max_length=150)
	item48 = models.CharField(null=True, blank=True, max_length=150)
	titulo5 = models.CharField(null=True, blank=True, max_length=150)
	item51 = models.CharField(null=True, blank=True, max_length=150)
	item52 = models.CharField(null=True, blank=True, max_length=150)
	titulo6 = models.CharField(null=True, blank=True, max_length=150)
	item61 = models.CharField(null=True, blank=True, max_length=150)
	item62 = models.CharField(null=True, blank=True, max_length=150)
	item63 = models.CharField(null=True, blank=True, max_length=150)
	titulo7 = models.CharField(null=True, blank=True, max_length=150)
	descricao7 = models.TextField(null=True, blank=True)
	titulo8 = models.CharField(null=True, blank=True, max_length=150)
	item81 = models.CharField(null=True, blank=True, max_length=150)
	item82 = models.CharField(null=True, blank=True, max_length=150)
	item83 = models.CharField(null=True, blank=True, max_length=150)
	item84 = models.CharField(null=True, blank=True, max_length=150)
	item85 = models.CharField(null=True, blank=True, max_length=150)
	item86 = models.CharField(null=True, blank=True, max_length=150)
	item87 = models.CharField(null=True, blank=True, max_length=150)
	item88 = models.CharField(null=True, blank=True, max_length=150)
	item89 = models.CharField(null=True, blank=True, max_length=150)
	item810 = models.CharField(null=True, blank=True, max_length=150)
	item811= models.CharField(null=True, blank=True, max_length=150)
	item812 = models.CharField(null=True, blank=True, max_length=150)
	item813 = models.CharField(null=True, blank=True, max_length=150)
	item814 = models.CharField(null=True, blank=True, max_length=150)
	item815 = models.CharField(null=True, blank=True, max_length=150)
	item816 = models.CharField(null=True, blank=True, max_length=150)
	item817 = models.CharField(null=True, blank=True, max_length=150)
	item818 = models.CharField(null=True, blank=True, max_length=150)
	item819 = models.CharField(null=True, blank=True, max_length=150)
	item820 = models.CharField(null=True, blank=True, max_length=150)
	item821 = models.CharField(null=True, blank=True, max_length=150)
	item822 = models.CharField(null=True, blank=True, max_length=150)
	item823= models.CharField(null=True, blank=True, max_length=150)	
	titulo9 = models.CharField(null=True, blank=True, max_length=150)
	item91 = models.CharField(null=True, blank=True, max_length=150)
	item92= models.CharField(null=True, blank=True, max_length=150)
	item93 = models.CharField(null=True, blank=True, max_length=150)
	item94= models.CharField(null=True, blank=True, max_length=150)
	item95= models.CharField(null=True, blank=True, max_length=150)

	def publish(self):
		self.save()

	def __str__(self):
		return self.nome