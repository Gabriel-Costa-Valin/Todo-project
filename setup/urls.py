from django.contrib import admin
from django.urls import path
from tarefas.views import TarefaListView, TarefaCreateView, TarefaUpdateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TarefaListView.as_view(), name="tarefa_list"),
    path("create/", TarefaCreateView.as_view(), name="tarefa_create"),
    path("update/<int:pk>", TarefaUpdateView.as_view(), name="tarefa_update"),
]
