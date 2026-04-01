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
    fields = "__all__"
    template_name = "task_manager/labels/update.html"
    extra_context = {"title": "Обнавление"}
    success_url = reverse_lazy("labels:list_labels")

    def form_valid(self, form):
        messages.success(
            self.request, 
            f"Метка {form.instance.label_name} успешно изменена"
        )
        return super().form_valid(form)


class DeleteLabel(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = "task_manager/labels/delete.html"
    extra_context = {"title": "Удаление"}
    success_url = reverse_lazy("labels:list_labels")
    
    def post(self, request, *args, **kwargs):
        label = self.get_object()
        labels_count = label.tasks.count()
        
        if labels_count > 0:
            messages.error(
                request, 
                "Невозможно удалить метку, потому что она используется")
            return redirect('labels:list_labels')
            
        messages.success(
                request, 
                "Метка успешно удалёна!")
        return super().post(request, *args, **kwargs)


class CreateLabel(LoginRequiredMixin, CreateView):
    form_class = CreateLabelForm
    template_name = "task_manager/labels/create.html"
    success_url = reverse_lazy("labels:list_labels")
    extra_context = {"title": "Создать метку", "button_name": "Создать"}

    def form_valid(self, form):
        messages.success(self.request, "Метка успешно создана")
        return super().form_valid(form)
    

