from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    descricao = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Pagina(models.Model):
    titulo = models.CharField(max_length=200, unique=True)

    # Slug para URLs amigáveis, ex: /wiki/sistemas-de-informacao
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='paginas')
    tags = models.ManyToManyField(Tag, related_name='paginas', blank=True)
    conteudo_atual = models.TextField(help_text="Utilize Markdown para formatar o texto.")
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='paginas_criadas')
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
