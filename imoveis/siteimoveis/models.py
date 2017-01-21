from django.db import models
from PIL import Image

class Vendedor(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    def __str__(self):
        return self.nome



class Imovel(models.Model):

    endereco = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='uploads/')
    vendedor = models.ForeignKey(Vendedor)
    valor = models.FloatField()
    bairro = models.CharField(max_length=100)
    anuncio = models.CharField(max_length=100)


    def __str__(self):
        return self.anuncio

    def image_tag(self):
        return u'<img src="%s" width="150" height="150"  />' %(self.imagem.url)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
