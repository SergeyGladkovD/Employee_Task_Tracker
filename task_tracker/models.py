from django.db import models

from employees.models import Employee

NULLABLE = {'blank': True, 'null': True}

TASK_STATUS = [
    ("create", "create"),
    ("start", "start"),
    ("finish", "finish"),
]

FATHER_TASK = [
    ('father', 'father'),
    ('other', 'other')
]


class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name", help_text="Введите наименование задачи")
    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, help_text="Введите родительскую задачу", **NULLABLE)
    executor = models.ForeignKey(Employee, verbose_name="Executor", related_name='tasks', on_delete=models.CASCADE, help_text="Введите исполнителя", **NULLABLE)
    deadline = models.DateField(verbose_name="Deadline", help_text="Введите срок исполнения")
    status = models.CharField(choices=TASK_STATUS, default=TASK_STATUS[0][0], verbose_name="Status", help_text="Введите статус")
    father_task = models.CharField(choices=FATHER_TASK, default=FATHER_TASK[0][1], verbose_name="Father task", help_text="Это главная задача")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
