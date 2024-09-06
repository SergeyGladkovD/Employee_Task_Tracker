from django.db.models import Q
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from employees.models import Employee
from task_tracker.models import Task
from task_tracker.serializers import TaskSerializer


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeTaskSerializer(TaskSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    active_tasks_count = SerializerMethodField()

    class Meta:
        model = Employee
        fields = ('id', 'full_name', 'post', 'tasks', 'active_tasks_count',)

    def get_active_tasks_count(self, obj):
        return obj.tasks.filter(status='start').count()
