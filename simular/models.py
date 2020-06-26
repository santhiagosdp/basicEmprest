from django.conf import settings
from django.db import models
from django.utils import timezone



class Simulacao(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    valor = models.CharField(max_length=200)
    parcelas = models.IntegerField()
    valorfinal = models.IntegerField()
    data = models.DateTimeField(default=timezone.now)
    
class Acesso(models.Model):
    data = models.DateTimeField(default=timezone.now)