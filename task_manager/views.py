from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import RegisterUserForm, LoginUserForm
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
from .models import Users
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(
        request,
        "index.html",
        {"text": "Kirill-Nikolaev",
         "title": ""},
    )
class CreateUser(CreateView):
    form_class = RegisterUserForm
    template_name = "register.html"
    success_url = reverse_lazy("login_user")


class UpdateUser(UpdateView):
    model = Users
    form_class = RegisterUserForm
    template_name = "update.html"
    success_url = reverse_lazy("list_users")


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"
    extra_context = {"title": "Менеджер задач Hexlet"}

    def get_success_url(self):
        return reverse_lazy("home")


class UsersList(ListView):
    model = Users
    template_name = "users.html"
    context_object_name = "users"


class DeleteUser(DeleteView):
    model = Users
    fields = "__all__"
    template_name = "delete.html"
    success_url = reverse_lazy("list_users")


class LogoutUser(View):

    def get(self, request, **kwargs):
        pass

    pass