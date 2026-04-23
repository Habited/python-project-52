from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import CreateTaskForm, ListTasksForm
from django.views.generic import (CreateView,
                                  ListView,
                                  UpdateView,
                                  DeleteView,
                                  DetailView)
from .models import Tasks
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class TasksList(ListView, LoginRequiredMixin):
    
    model = Tasks
    template_name = "task_manager/tasks/tasks.html"
    context_object_name = "tasks"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = ListTasksForm(self.request.GET)
        context['title'] = 'Задачи'
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = ListTasksForm(self.request.GET)

        if form.is_valid():

            status = form.cleaned_data.get('status')
            if status:
                queryset = queryset.filter(status=status)

            executor = form.cleaned_data.get('executor')
            if executor:
                queryset = queryset.filter(executor=executor)

            label = form.cleaned_data.get('labels')
            if label:
                queryset = queryset.filter(labels=label)

            only_my = form.cleaned_data.get('author')
            if only_my:
                queryset = queryset.filter(author=self.request.user)

        return queryset


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Tasks
    form_class = CreateTaskForm
    template_name = "task_manager/tasks/update.html"
    extra_context = {"title": "Редактирование задачи"}
    success_url = reverse_lazy("tasks:list_tasks")

    def form_valid(self, form):
        messages.success(
            self.request, 
            "Задача успешно изменена"
        )
        return super().form_valid(form)


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Tasks
    template_name = "task_manager/tasks/delete.html"
    success_url = reverse_lazy("tasks:list_tasks")
    extra_context = {"title": "Удаление Задачи"}
    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.author != self.request.user:
            messages.error(request, "Задачу может удалить только ее автор")
            return redirect('tasks:list_tasks')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.success(
            self.request, 'Задача успешно удалена'
        )
        return super().form_valid(form)


class CreateTask(LoginRequiredMixin, CreateView):
    model = Tasks
    form_class = CreateTaskForm
    template_name = "task_manager/tasks/create.html"
    success_url = reverse_lazy("tasks:list_tasks")
    extra_context = {"title": "Создать задачу"}

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(
            self.request, 'Задача успешно создана'
        )
        return super().form_valid(form)
    

class ShowTask(LoginRequiredMixin, DetailView, ):
    
    model = Tasks
    template_name = "task_manager/tasks/task.html"
    context_object_name = "task"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Просмотр задачи'
        return context
    

