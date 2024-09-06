from django.urls import path
from employees.apps import EmployeesConfig
from employees.views import EmployeeCreateAPIView, EmployeeListAPIView, EmployeeRetrieveAPIView, EmployeeUpdateAPIView, \
    EmployeeDestroyAPIView, EmployeeTaskListAPIView

app_name = EmployeesConfig.name

urlpatterns = [
    path('create/', EmployeeCreateAPIView.as_view(), name='employee_create'),
    path('list/', EmployeeListAPIView.as_view(), name='employee_list'),
    path('<int:pk>/', EmployeeRetrieveAPIView.as_view(), name='employee_retrieve'),
    path('update/<int:pk>/', EmployeeUpdateAPIView.as_view(), name='employee_update'),
    path('delete/<int:pk>/', EmployeeDestroyAPIView.as_view(), name='employee_delete'),
    path('employee_task/', EmployeeTaskListAPIView.as_view(), name='employee_task'),
]
