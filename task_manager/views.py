from django.views.generic import TemplateView
from django.contrib.auth import views, logout

from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"


class LoginUser(views.LoginView):
    template_name = "task_manager/users/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Вход"
        return context
    
    def get_success_url(self):
        messages.success(self.request, "Вы залогинены")
        return reverse_lazy("home")
    
    
    def form_invalid(self, form):
        messages.error(self.request, 
            "Неверный логин или пароль"
        )
        return super().form_invalid(form)
    

def logout_view(request):
    logout(request)
    messages.success(request, "Вы разлогинены")
    return redirect("home")