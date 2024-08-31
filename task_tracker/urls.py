from django.urls import path
from task_tracker.apps import TaskTrackerConfig
from task_tracker.views import TaskCreateAPIView, TaskListAPIView, TaskRetrieveAPIView, TaskUpdateAPIView, TaskDestroyAPIView

app_name = TaskTrackerConfig.name

urlpatterns = [
    path('task/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('task/list/', TaskListAPIView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskRetrieveAPIView.as_view(), name='task-retrieve'),
    path('task/update/<int:pk>/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', TaskDestroyAPIView.as_view(), name='task-destroy'),

]
