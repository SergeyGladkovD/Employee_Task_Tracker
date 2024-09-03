from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from task_tracker.models import Task
from task_tracker.validators import NameValidator


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        validators = [
            NameValidator(field='name'),
            UniqueTogetherValidator(fields=['name'], queryset=Task.objects.all()),
        ]
