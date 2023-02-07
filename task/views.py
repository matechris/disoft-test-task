from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Task
from .permissions import IsAuthenticatedOrIsAdmin
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status"]
    permission_classes = [IsAuthenticatedOrIsAdmin,]
