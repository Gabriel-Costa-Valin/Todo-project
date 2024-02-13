from django.db import models

# Create your models here.


class Tarefa(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    entrega = models.DateTimeField(null=False, blank=False)
    terminada_em = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.titulo
