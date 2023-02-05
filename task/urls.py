from django.urls import include, path
from rest_framework import routers

from task.views import TaskViewSet

router = routers.DefaultRouter()
router.register("", TaskViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "task"
