# tasks/urls.py
from django.urls import path
from . import views
from .views import create_task, update_task, delete_task, signup, dashboard

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("create/", create_task, name="create_task"),
    path("update/<int:pk>/", update_task, name="update_task"),
    path("delete/<int:pk>/", delete_task, name="delete_task"),
    path("signup/", signup, name="signup"),
    path("dashboard/", dashboard, name="dashboard"),
    # path("create/", TaskCreateView.as_view(), name="create_task"),
]
