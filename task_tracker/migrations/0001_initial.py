# Generated by Django 5.1 on 2024-09-08 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("employees", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименование задачи",
                        max_length=100,
                        verbose_name="Name",
                    ),
                ),
                (
                    "deadline",
                    models.DateField(
                        blank=True,
                        help_text="Введите срок исполнения",
                        null=True,
                        verbose_name="Deadline",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("start", "start"), ("finish", "finish")],
                        default="start",
                        help_text="Введите статус",
                        verbose_name="Status",
                    ),
                ),
                (
                    "executor",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите исполнителя",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="employees.employee",
                        verbose_name="Executor",
                    ),
                ),
                (
                    "parent_task",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите родительскую задачу",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="other",
                        to="task_tracker.task",
                    ),
                ),
            ],
            options={
                "verbose_name": "Task",
                "verbose_name_plural": "Tasks",
            },
        ),
    ]
