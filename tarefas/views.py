from django.shortcuts import render
from .models import Tarefa

# Create your views here.


def tarefa_list(request):
    tarefas = Tarefa.objects.all()
    return render(request, "tarefas/tarefa_list.html", {"tarefas": tarefas})
