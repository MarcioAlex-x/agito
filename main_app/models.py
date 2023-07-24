from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    resumo = models.TextField(max_length=200)
    conteudo = RichTextUploadingField()
    imagem_post = models.ImageField(upload_to='images/',blank=True, null=True)
    imagens_de = models.CharField(max_length=50)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Publicado em')
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo



