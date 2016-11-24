from django.db import models
from django.utils import timezone

class PostManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(title__icontains=query) | \
            models.Q(text__icontains=query)
        )

class Post(models.Model):

    CATEGORIAS_POST = (     
        ('concurso', 'Concurso do Departamento de Engenharia de Transportes e Geodésia'),
        ('monitoria', 'Monitoria'),
        ('estagio', 'Estágio'),
        ('viagem', 'Viagem para atividades acadêmica'),
        ('congresso', 'Congresso'),
        ('seminario', 'Seminário'),
        ('simposio', 'Simpósio'),
        ('artigo', 'Artigo'),
    )

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    imagem = models.ImageField(null=True, blank=True, upload_to='noticia')    
    text = models.TextField()
    topico = models.CharField(max_length=200, null=True, blank=True, choices=CATEGORIAS_POST)
    link = models.CharField(max_length=200, null=True, blank=True)
    local = models.CharField(max_length=200, null=True, blank=True)
    data = models.CharField(max_length=200, null=True, blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    objects = PostManager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('noticias:details', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['title']

class Principal(models.Model):
    post_principal = models.ForeignKey(Post)

    def publish(self):        
        self.save()

    def __str__(self):
        return self.post_principal.title

    class Meta:
        verbose_name = 'Principal'
        verbose_name_plural = 'Principais'
        


