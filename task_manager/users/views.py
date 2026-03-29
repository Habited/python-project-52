from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import RegisterUserForm, LoginUserForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from task_manager.tasks.models import Tasks
from django.db.models import ProtectedError


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "task_manager/users/register.html"
    extra_context = {"title": "Регистрация"}

    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно зарегистрирован")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(
            self.request, 
            "Проверьте правильность заполнения формы"
        )
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("users:login_user")


class UpdateUser(UpdateView):
    model = User
    fields = ["last_name", "first_name", "username"]
    template_name = "task_manager/users/update.html"
    extra_context = {"title": "Обнавление"}
    success_url = reverse_lazy("users:list_users")

    def form_valid(self, form):
        messages.success(
            self.request, 
            f"Пользователь {form.instance.username} успешно изменен"
        )
        return super().form_valid(form)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "task_manager/users/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Вход"
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Вы залогинены")
        return super().form_valid(form)
    
    
    def form_invalid(self, form):
        messages.error(
            self.request, 
            "Проверьте правильность заполнения формы"
        )
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("home")
    

class LogoutUser(LogoutView):
    
    http_method_names = ['post',]
    next_page = reverse_lazy('users:login_user')
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Вы разлогинены")
        return super().dispatch(request, *args, **kwargs)


class UsersList(ListView):
    model = User
    context_object_name = 'users'
    template_name = "task_manager/users/users.html"
    extra_context = {"title": "Пользователи"}


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "task_manager/users/delete.html"
    success_url = reverse_lazy("users:list_users")
    
    def post(self, request, *args, **kwargs):
        user = self.get_object()
        author_task_count = Tasks.objects.filter(author=user).count()

        if author_task_count > 0:
            messages.error(request,
                f"Нельзя удалить пользователя {user.username}, если он связан с задачами.")
            return redirect('users:list_users')
        
        messages.success(request, "Пользователь удалён")
        return super().post(request, *args, **kwargs)
