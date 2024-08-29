from rest_framework import viewsets

from task_tracker.models import Task
from task_tracker.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
