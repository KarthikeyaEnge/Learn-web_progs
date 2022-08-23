from django.shortcuts import render
from .models import train
# Create your views here.
def index(request):
    return render(request,'Train/index.html',{
        'trains':train.objects.all()
    })