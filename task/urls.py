from django.urls import include, path

from task.views import TaskList, TaskDetail


urlpatterns = [
    path("", TaskList.as_view(), name="task-list"),
    path("<int:pk>/", TaskDetail.as_view(), name="task-detial")
]

app_name = "task"
