from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    imagem = models.ImageField(null=True, blank=True, upload_to='noticia')    
    text = models.TextField()
    topico = models.CharField(max_length=200, null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)    
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Principal(models.Model):
    post_principal = models.ForeignKey(Post)

    def publish(self):        
        self.save()

    def __str__(self):
        return self.post_principal.title


