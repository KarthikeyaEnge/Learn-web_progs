from django.shortcuts import render
import datetime
# Create your views here.
date=datetime.datetime.now()
def index(request):
    return render(request,'page2/date.html',{
        "date":str(date.day)+'/'+str(date.month)+'/'+str(date.year)
    })

def isityogaday(request):
    return render(request,'page2/isityogaday.html',{
        'msg':date.month=='6' and date.day=='21'
    })    

def evendate(request):
    return render(request, 'page2/evendate.html',{
        'msg':date.day%2==0
    })