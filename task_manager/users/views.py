from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form
            user.save()
            return redirect("users:login_user")
    else:
        form = RegisterUserForm()
    return render(request, "task_manager/users/register.html", {"title": "Регистрация", "button_name": "Зарегистрировать", "form": form})


class UpdateUser(UpdateView):
    model = User
    form_class = RegisterUserForm
    template_name = "task_manager/users/update.html"
    extra_context = {"title": "Обнавление"}
    success_url = reverse_lazy("users:list_users")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "task_manager/users/login.html"
    extra_context = {"title": "Вход"}

    def get_success_url(self):
        return reverse_lazy("home")


class UsersList(ListView):
    model = User
    context_object_name = 'users'
    fields = "__all__"
    template_name = "task_manager/users/users.html"
    extra_context = {"title": "Пользователи"}


class DeleteUser(DeleteView):
    model = User
    fields = "__all__"
    template_name = "task_manager/users/delete.html"
    extra_context = {"title": "Удаление"}
    success_url = reverse_lazy("users:list_users")