from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employees.models import Employee


class EmployeeTestCase(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(full_name='Тест имя', post='Тест должность')

    def test_employee_create(self):
        url = reverse('employees:employee_create')
        data = {'full_name': 'Гладков Сергей', 'post': 'developer'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['full_name'], 'Гладков Сергей')
        self.assertEqual(response.data['post'], 'developer')
        self.assertEqual(Employee.objects.count(), 2)

    def test_employee_retrieve(self):
        url = reverse('employees:employee_retrieve', args=(self.employee.id,))
        response = self.client.get(url, format='json')
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['full_name'], self.employee.full_name)
        self.assertEqual(data['post'], self.employee.post)

    def test_employee_update(self):
        url = reverse('employees:employee_update', args=(self.employee.id,))
        response = self.client.patch(url, data={'full_name': 'updated name', 'post': 'update developer'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], 'updated name')
        self.assertEqual(response.data['post'], 'update developer')

    def test_employee_delete(self):
        url = reverse('employees:employee_delete', args=(self.employee.id,))
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)

    def test_employee_list(self):
        url = reverse('employees:employee_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.count(), 1)
