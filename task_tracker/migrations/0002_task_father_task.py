# Generated by Django 5.1 on 2024-08-28 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task_tracker", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="father_task",
            field=models.CharField(
                choices=[("father", "father"), ("other", "other")],
                default="father",
                help_text="Это главная задача",
                verbose_name="Father task",
            ),
        ),
    ]
