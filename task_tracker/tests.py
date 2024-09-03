from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from task_tracker.models import Task


class TaskTestCase(APITestCase):
    def setUp(self):
        self.task = Task.objects.create(name='Тест задача', parent_task=None, executor=None, deadline='2024-09-12', status='start', father_task='other')

    def test_task_create(self):
        url = reverse('task_tracker:task-create')
        data = {'name': 'Написать программу', 'parent_task': None, 'executor': None, 'deadline': '2024-12-12', 'status': 'start', 'father_task': 'other'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Написать программу')
        self.assertEqual(response.data['parent_task'], None)
        self.assertEqual(response.data['executor'], None)
        self.assertEqual(response.data['deadline'], '2024-12-12')
        self.assertEqual(response.data['status'], 'start')
        self.assertEqual(response.data['father_task'], 'other')
        self.assertEqual(Task.objects.count(), 2)

    def test_task_retrieve(self):
        url = reverse('task_tracker:task-retrieve', args=(self.task.id,))
        response = self.client.get(url, format='json')
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['name'], self.task.name)
        self.assertEqual(data['parent_task'], self.task.parent_task)
        self.assertEqual(data['executor'], self.task.executor)
        self.assertEqual(data['deadline'], self.task.deadline)
        self.assertEqual(data['status'], self.task.status)
        self.assertEqual(data['father_task'], self.task.father_task)

    def test_task_update(self):
        url = reverse('task_tracker:task-update', args=(self.task.id,))
        response = self.client.patch(url, {'name': 'update task'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'update task')

    def test_task_delete(self):
        url = reverse('task_tracker:task-delete', args=(self.task.id,))
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_task_list(self):
        url = reverse('task_tracker:task-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)
