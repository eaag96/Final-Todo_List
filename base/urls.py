from sys import implementation
from django.urls import path
from .views import TaskDetail, TaskList
from base import views

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
]
