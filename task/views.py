from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
