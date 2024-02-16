from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .models import Tarefa
from django.shortcuts import get_object_or_404, redirect
from datetime import date

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


class TarefaDeleteView(DeleteView):
    model = Tarefa
    success_url = reverse_lazy("tarefa_list")


class TarefaCompleteView(View):
    def get(self, request, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        Tarefa.mark_has_complete()
        return redirect("tarefa_list")
