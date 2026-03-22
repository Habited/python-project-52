from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from task_manager.users import views

app_name = "users"

urlpatterns = [ 
    path('register/', views.register, name='register_user'),
    path('', views.UsersList.as_view(), name='list_users'),
    path('<int:pk>/update/', views.UpdateUser.as_view(), name='update_user'),
    path('<int:pk>/delete/', views.DeleteUser.as_view(), name='delete_user'),
    path('login/', views.LoginUser.as_view(), name='login_user'),
    path('logout/', LogoutView.as_view(http_method_names=['get', 'post'], next_page='/users/login/'), name='logout_user'),
]