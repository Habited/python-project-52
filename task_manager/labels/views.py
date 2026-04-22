from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.labels.forms import CreateLabelForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.labels.models import Label


class LabelsList(LoginRequiredMixin, ListView):
    model = Label
    template_name = "task_manager/labels/labels.html"
    context_object_name = "labels"
    extra_context = {"title": "Метки"}


class UpdateLabel(LoginRequiredMixin, UpdateView):
    model = Label
    fields = ['label_name']
    template_name = "task_manager/labels/update.html"
    extra_context = {"title": "Обнавление"}
    success_url = reverse_lazy("labels:list_labels")

    def form_valid(self, form):
        messages.success(
            self.request, 
            f"Метка успешно изменена"
        )
        return super().form_valid(form)


class DeleteLabel(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = "task_manager/labels/delete.html"
    extra_context = {"title": "Удаление"}
    success_url = reverse_lazy("labels:list_labels")
    
    def form_valid(self, form):
        if self.object.tasks.exists():
            messages.error(self.request, 'Невозможно удалить метку')
            return redirect(self.success_url)

        messages.success(self.request, 'Метка успешно удалена')
        return super().form_valid(form)


class CreateLabel(LoginRequiredMixin, CreateView):
    form_class = CreateLabelForm
    template_name = "task_manager/labels/create.html"
    success_url = reverse_lazy("labels:list_labels")
    extra_context = {"title": "Создать метку"}

    def form_valid(self, form):
        messages.success(self.request, "Метка успешно создана")
        return super().form_valid(form)
    

