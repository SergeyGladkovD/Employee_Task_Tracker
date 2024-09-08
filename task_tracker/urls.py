from django.urls import path
from task_tracker.apps import TaskTrackerConfig
from task_tracker.views import TaskCreateAPIView, TaskListAPIView, TaskRetrieveAPIView, TaskUpdateAPIView, \
    TaskDestroyAPIView, TaskImportantListAPIView

app_name = TaskTrackerConfig.name

urlpatterns = [
    path('create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('list/', TaskListAPIView.as_view(), name='task-list'),
    path('<int:pk>/', TaskRetrieveAPIView.as_view(), name='task-retrieve'),
    path('update/<int:pk>/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDestroyAPIView.as_view(), name='task-delete'),
    path('tracker/', TaskImportantListAPIView.as_view(), name='tracker'),
]
