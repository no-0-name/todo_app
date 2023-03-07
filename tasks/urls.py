from django.urls import path
from . import views


urlpatterns = [
    path("", views.TaskList, name="list"),
    path("update/<int:pk>/", views.TaskUpdate, name="update"),
    path("delete/<int:pk>/", views.TaskDelete, name="delete"),
]
