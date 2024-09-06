from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from employees.models import Employee
from employees.serializers import EmployeeSerializer, EmployeeTaskSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from task_tracker.models import Task


class EmployeeCreateAPIView(CreateAPIView):
    serializer_class = EmployeeSerializer


class EmployeeListAPIView(ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveAPIView(RetrieveAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeUpdateAPIView(UpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDestroyAPIView(DestroyAPIView):
    queryset = Employee.objects.all()


class EmployeeTaskListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeTaskSerializer

    def get_queryset(self):
        return (Employee.objects.annotate(
            active_tasks_count=Count('tasks', filter=Q(tasks__status='start'))
        )
                .filter(active_tasks_count__gt=0)
                .order_by('-active_tasks_count'))
