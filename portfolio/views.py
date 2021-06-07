from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request,'portfolio/home.html',{'projects':projects})

def base1(request):
    projects = Project.objects.all()
    return render(request,'portfolio/base1.html',{'projects':projects})