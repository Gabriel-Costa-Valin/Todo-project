from django.db import models
from datetime import date

# Create your models here.


class Tarefa(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    criado_em = models.DateField(auto_now_add=True, null=False, blank=False)
    entrega = models.DateField(null=False, blank=False)
    terminada_em = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["entrega"]


    def mark_has_complete(self):
        if not self.terminada_em:
            self.terminada_em = date.today()
            self.save()


    def __str__(self) -> str:
        return self.titulo
