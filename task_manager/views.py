from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import RegisterUserForm, LoginUserForm, CreateStatusForm
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
from .models import Users, Statuses
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(
        request,
        "index.html",
        {"text": "Kirill-Nikolaev",
         "title": ""}
    )
class CreateUser(CreateView):
    form_class = RegisterUserForm
    template_name = "register.html"
    extra_context = {"title": "Регистрация", "button_name": "Зарегестрировать"}
    success_url = reverse_lazy("login_user")


class UpdateUser(UpdateView):
    model = Users
    form_class = RegisterUserForm
    template_name = "update.html"
    extra_context = {"title": "Обнавление"}
    success_url = reverse_lazy("list_users")


class LoginUser(LoginView):
    model = Users
    form_class = AuthenticationForm
    template_name = "login.html"
    extra_context = {"title": "Вход"}

    def get_success_url(self):
        return reverse_lazy("home")


class UsersList(ListView):
    model = Users
    template_name = "users.html"
    context_object_name = "users"
    extra_context = {"title": "Пользователи"}


class DeleteUser(DeleteView):
    model = Users
    fields = "__all__"
    template_name = "delete.html"
    extra_context = {"title": "Удаление"}
    success_url = reverse_lazy("list_users")


class StatusesList(LoginRequiredMixin, ListView):
    model = Statuses
    template_name = "statuses.html"
    context_object_name = "statuses"
    extra_context = {"title": "Статусы"}
    login_url = reverse_lazy("login_user")


class UpdateStatus(UpdateView):
    model = Statuses
    fields = "__all__"
    template_name = "update.html"
    extra_context = {"title": "Обнавление"}
    success_url = reverse_lazy("list_statuses")


class DeleteStatus(DeleteView):
    model = Statuses
    fields = "__all__"
    template_name = "delete.html"
    extra_context = {"title": "Удаление"}
    success_url = reverse_lazy("list_statuses")


class CreateStatus(CreateView):
    form_class = CreateStatusForm
    template_name = "register.html"
    extra_context = {"title": "Создать статус", "button_name": "Создать"}
    success_url = reverse_lazy("list_statuses")