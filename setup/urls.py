from django.contrib import admin
from django.urls import path
from tarefas.views import tarefa_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", tarefa_list, name="tarefa_list"),
]
