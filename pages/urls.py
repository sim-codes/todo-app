from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("<int:pk>/delete", views.TodoDeleteView.as_view(), name="todo_delete"),
]
