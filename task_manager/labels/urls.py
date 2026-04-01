from django.urls import path
from task_manager.labels import views

app_name = "labels"

urlpatterns = [
    path('', views.LabelsList.as_view(), name='list_labels'),
    path('<int:pk>/update/', views.UpdateLabel.as_view(), name='update_label'),
    path('<int:pk>/delete/', views.DeleteLabel.as_view(), name='delete_label'),
    path('create/', views.CreateLabel.as_view(), name='create_label'),
]
