from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Tarefa

# Create your views here.


class TarefaListView(ListView):
    model = Tarefa


class TarefaCreateView(CreateView):
    model = Tarefa
    fields = ["titulo", "entrega"]
    success_url = reverse_lazy("tarefa_list")
    

class TarefaUpdateView(UpdateView):
    model = Tarefa
    fields = ["titulo", "entrega"]
    success_url = reverse_lazy("tarefa_list")