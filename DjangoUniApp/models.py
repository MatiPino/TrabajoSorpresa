from django.db import models

class Recordatorios(models.Model):
    fechainicio = models.DateTimeField(auto_now=True)
    fechafinal = models.DateField('Fecha hasta')
    asunto = models.CharField(max_length=100, blank=False, null=False)
    texto = models.TextField(max_length=200, blank=False, null=False)
    estado = models.BooleanField(default=0)
