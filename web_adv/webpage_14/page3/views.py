from django.urls import reverse
from unicodedata import name
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

anime=['Naruto', 'Blakclover', 'onepiece', 'Fairytail', 'Re:Zero']

class newform(forms.Form):
    ani=forms.CharField(label="New Anime")

def index(request):

     return render(request,'page3/List.html',{
        'anime':anime
     })

def add(request):
 
    if(request.method=='POST'):
        form=newform(request.POST)
        if(form.is_valid()):
            ani=form.cleaned_data['ani']
            anime.append(ani)

            return HttpResponseRedirect(reverse("page3:index"))
        else:
            return render(request,'page3/add.html',{
                'form':form
            })    


    return render(request,'page3/add.html',{
        'form':newform()
    })    
