from django.shortcuts import render
from api.models import Task
# Create your views here.
def index(request):
    task = Task.objects.all()
    return render(request, 'frontend/index.html')