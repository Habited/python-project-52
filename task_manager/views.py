from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import RegisterUserForm, LoginUserForm 
from django.views.generic import View, FormView


def index(request):
    return render(
        request,
        "index.html",
        {"text": "Kirill-Nikolaev",
         "title": ""},
    )

class UserRegister(FormView):
    form_class = RegisterUserForm
    template_name = "register.html"
    success_url = reverse_lazy('register')



def login(request):
    if request.method == "post":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = LoginUserForm()
    return render(
        request,
        "login.html",
        {"form": form,
        "title": "Менеджер задач Hexlet",
        }
    )

class Users(View):

    def get(self, reuqest):
        database: list[dict] = [
            {"id" : 1, "name": "Vague", "user_name": "Big Vague", "create_date": "11.11.2011"},
            {"id" : 1, "name": "Vague", "user_name": "Big Vague", "create_date": "11.11.2011"}
        ]
        data = {
            "users": database
        }
        return render(reuqest, 'users.html', context=data)