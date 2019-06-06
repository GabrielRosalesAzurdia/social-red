from django.db import models

# Create your models here.

class Perfil(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    publicaciones = models.TextField()
    cover = models.ImageField(upload_to='images/')
    seguidores = models.IntegerField(default=0)
    seguitores_nombres = models.TextField(default='')

    def __str__(self):
        return self.nombre