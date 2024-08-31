from django.urls import path
from employees.apps import EmployeesConfig
from employees.views import EmployeeCreateAPIView, EmployeeListAPIView, EmployeeRetrieveAPIView, EmployeeUpdateAPIView, EmployeeDestroyAPIView

app_name = EmployeesConfig.name

urlpatterns = [
    path('employee/create/', EmployeeCreateAPIView.as_view(), name='employee_create'),
    path('employee/list/', EmployeeListAPIView.as_view(), name='employee_list'),
    path('employee/<int:pk>/', EmployeeRetrieveAPIView.as_view(), name='employee_retrieve'),
    path('employee/update/<int:pk>/', EmployeeUpdateAPIView.as_view(), name='employee_update'),
    path('employee/delete/<int:pk>/', EmployeeDestroyAPIView.as_view(), name='employee_delete'),

]
