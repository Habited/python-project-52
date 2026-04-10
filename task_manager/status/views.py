from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import CreateStatusForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Statuses
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.tasks.models import Tasks


class StatusesList(LoginRequiredMixin, ListView):
    model = Statuses
    template_name = "task_manager/status/statuses.html"
    context_object_name = "statuses"
    extra_context = {"title": "Статусы"}


class UpdateStatus(LoginRequiredMixin, UpdateView):
    model = Statuses
    fields = ['status_name']
    template_name = "task_manager/status/update.html"
    extra_context = {"title": "Обнавление"}
    success_url = reverse_lazy("statuses:list_statuses")

    def form_valid(self, form):
        messages.success(
            self.request, 
            f"Статус успешно изменен"
        )
        return super().form_valid(form)


class DeleteStatus(LoginRequiredMixin, DeleteView):
    model = Statuses
    template_name = "task_manager/status/delete.html"
    extra_context = {"title": "Удаление"}
    success_url = reverse_lazy("statuses:list_statuses")
    
    def post(self, request, *args, **kwargs):
        status = self.get_object()
        tasks_count = Tasks.objects.filter(status=status).count()
        
        if tasks_count > 0:
            messages.error(
                request, 
                "Невозможно удалить статус, потому что он используется")
            return redirect('statuses:list_statuses')
            
        messages.success(
                request, 
                "Статус успешно удален")
        return super().post(request, *args, **kwargs)


class CreateStatus(LoginRequiredMixin, CreateView):
    form_class = CreateStatusForm
    template_name = "task_manager/status/create_status.html"
    success_url = reverse_lazy("statuses:list_statuses")
    extra_context = {"title": "Создать статус"}

    def form_valid(self, form):
        messages.success(self.request, "Статус успешно создан")
        return super().form_valid(form)
    

