from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from task_manager.tasks.models import Tasks
from django.db.models import ProtectedError
from django.views.generic.edit import FormView
from task_manager.users.forms import RegisterUserForm, UpdateUserForm


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "task_manager/users/register.html"
    extra_context = {"title": "Регистрация"}

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Пользователь успешно зарегистрирован")
        return response
    
    def form_invalid(self, form):
        messages.error(
            self.request, 
            "Проверьте правильность заполнения формы"
        )
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("login_user")


class UpdateUser(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = "task_manager/users/update.html"
    extra_context = {"title": "Обновление"}
    success_url = reverse_lazy("users:list_users")
    
    def get_object(self, queryset=None):
        return User.objects.get(pk=self.kwargs['pk'])
    
    def form_valid(self, form):
        if self.request.user != self.get_object():
            messages.error(self.request, "У вас нет прав для изменения")
            return redirect('users:list_users')
        
        messages.success(self.request, "Пользователь успешно изменен")
        return super().form_valid(form)


class UsersList(ListView, LoginRequiredMixin):
    model = User
    context_object_name = 'users'
    template_name = "task_manager/users/users.html"
    extra_context = {"title": "Пользователи"}


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "task_manager/users/delete.html"
    success_url = reverse_lazy("users:list_users")
    
    def form_valid(self, form):
        if self.request.user != self.object:
            messages.error(self.request,
                "Вы не можете удалить другого пользователя")
            return redirect('users:list_users')
        if (self.object.author_tasks.exists() or 
            self.object.executor_tasks.exists()
        ):
            messages.error(
                self.request,
                'Невозможно удалить пользователя,'
                ' потому что он используется',
            )
            return redirect('users:list_users')

        messages.success(self.request, "Пользователь успешно удален")
        return super().form_valid(form)

