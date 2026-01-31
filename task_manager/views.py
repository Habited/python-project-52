from django.shortcuts import render
from .forms import RegisterUserForm, LoginUserForm 


def index(request):
    return render(
        request,
        "index.html",
        {"text": "Kirill-Nikolaev",
         "title": ""},
    )

def register(request):
    if request.method == "post":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(
        request,
        "register.html",
        {"form": form,
        "title": "Менеджер задач Hexlet",
        }
    )

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