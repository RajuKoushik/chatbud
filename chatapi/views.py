from django.shortcuts import render

# Create your views here.
from .models import *


def home(request):
    groups = Group.objects.all()
    return render(request, 'chatapi/home.html', {'groups': groups})
