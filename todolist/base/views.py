from django.views.generic import ListView
from .models import Task
# Create your views here.


class TaskList(ListView):
    model = Task
