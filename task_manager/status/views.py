from django.urls import reverse_lazy
from .forms import CreateStatusForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Statuses
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class StatusesList(LoginRequiredMixin, ListView):
    model = Statuses
    fields = "__all__"
    template_name = "task_manager/status/statuses.html"
    context_object_name = "statuses"
    extra_context = {"title": "Статусы"}


class UpdateStatus(UpdateView):
    model = Statuses
    fields = "__all__"
    template_name = "task_manager/status/update.html"
    extra_context = {"title": "Обнавление"}
    success_url = reverse_lazy("statuses:list_statuses")


class DeleteStatus(DeleteView):
    model = Statuses
    template_name = "task_manager/status/delete.html"
    extra_context = {"title": "Удаление"}
    success_url = reverse_lazy("statuses:list_statuses")


class CreateStatus(LoginRequiredMixin, CreateView):
    form_class = CreateStatusForm
    template_name = "task_manager/status/create_status.html"
    success_url = reverse_lazy("statuses:list_statuses")
    extra_context = {"title": "Создать статус", "button_name": "Создать"}
