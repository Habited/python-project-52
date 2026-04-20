from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import RegisterUserForm, LoginUserForm, UpdateUserForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from task_manager.tasks.models import Tasks
from django.db.models import ProtectedError
from django.views.generic.edit import FormView

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


class UpdateUser(UpdateView):
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
        
        messages.success(self.request, "Пользователь успешно изменён")
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
    next_page = reverse_lazy('login_user')
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Вы разлогинены")
        return super().dispatch(request, *args, **kwargs)


class UsersList(ListView, LoginRequiredMixin):
    model = User
    context_object_name = 'users'
    template_name = "task_manager/users/users.html"
    extra_context = {"title": "Пользователи"}


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "task_manager/users/delete.html"
    success_url = reverse_lazy("users:list_users")
    
    def post(self, request, pk, *args, **kwargs):
        user = User.objects.get(pk=pk)

        if self.request.user != user:
            messages.error(request,
                f"У вас нет прав для")
            return redirect('users:list_users')
        messages.success(request, "Пользователь успешно удалён")
        return super().post(request, *args, **kwargs)

