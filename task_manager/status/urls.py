from django.urls import path
from task_manager.status import views

app_name = "statuses"

urlpatterns = [
    path('',
         views.StatusesList.as_view(),
         name='list_statuses'),
    path('<int:pk>/update/',
         views.UpdateStatus.as_view(),
         name='update_status'),
    path('<int:pk>/delete/',
         views.DeleteStatus.as_view(),
         name='delete_status'),
    path('create/',
         views.CreateStatus.as_view(),
         name='create_status'),
]
