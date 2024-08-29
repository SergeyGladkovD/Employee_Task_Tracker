from rest_framework.routers import SimpleRouter

from task_tracker.apps import TaskTrackerConfig
from task_tracker.views import TaskViewSet

app_name = TaskTrackerConfig.name
router = SimpleRouter()
router.register('', TaskViewSet, basename='tasks')

urlpatterns = [

] + router.urls
