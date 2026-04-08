from django.shortcuts import render
from django .http import HttpResponse
from .models import Coffee
def index(request):
    coffee = Coffee.objects.all()
    return render(request,'home.html',{'coffee':coffee})


# Create your views here.
