from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True) # Criar um id sequencial e não duplicavel que vai representar cada usuario
    nome = models.TextField(max_length=255) #maximo de caracteres
    idade = models.IntegerField() # um inteiro