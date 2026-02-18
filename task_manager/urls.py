"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('users/', views.UsersList.as_view(), name='list_users'),
    path('users/create/', views.CreateUser.as_view(), name='register_user'),
    path('users/<int:pk>/update', views.UpdateUser.as_view(), name='update_user'),
    path('users/<int:pk>/delete', views.DeleteUser.as_view(), name='delete_user'),
    path('login/', views.LoginUser.as_view(), name='login_user'),
    path('logout', views.LogoutUser.as_view(), name='logout_user'),
]
