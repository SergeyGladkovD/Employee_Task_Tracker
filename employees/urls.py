from rest_framework.routers import SimpleRouter
from employees.apps import EmployeesConfig
from employees.views import EmployeeViewSet

app_name = EmployeesConfig.name
router = SimpleRouter()
router.register('', EmployeeViewSet, basename='employees')

urlpatterns = [

] + router.urls
