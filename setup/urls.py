from django.contrib import admin
from django.urls import path
from tarefas.views import (
    TarefaListView,
    TarefaCreateView,
    TarefaUpdateView,
    TarefaDeleteView,
    TarefaCompleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TarefaListView.as_view(), name="tarefa_list"),
    path("create/", TarefaCreateView.as_view(), name="tarefa_create"),
    path("update/<int:pk>", TarefaUpdateView.as_view(), name="tarefa_update"),
    path("delete/<int:pk>", TarefaDeleteView.as_view(), name="tarefa_delete"),
    path("complete/<int:pk>", TarefaCompleteView.as_view(), name="tarefa_complete"),
]
