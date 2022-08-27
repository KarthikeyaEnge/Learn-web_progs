from asyncio.windows_events import NULL
from audioop import reverse
from itertools import count
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from .models import train,station,customer,booking
# Create your views here.

gen=[('male','male'),('female','female'),('other','others')]

class newform(forms.Form):
    user=forms.CharField(label='Username')
    pa=forms.CharField(label='password',widget=forms.PasswordInput)


class su_newform(forms.Form):
        first=forms.CharField(label='Name')
        user=forms.CharField(label='Username')
        pa=forms.CharField(label='password',widget=forms.PasswordInput)
        dob=forms.DateField(label='D.O.B')
        gender=forms.CharField(widget=forms.RadioSelect(choices=gen))
        ph=forms.IntegerField()



def index(request):
    return render(request,'Train/index.html',{
        'trains':train.objects.all()
    })

#not completed yet need to add his booking history
def sign_in(request):
    if(request.method=='POST'):
        form=newform(request.POST)
        if(form.is_valid()):
            user=form.cleaned_data['user']
            pa=form.cleaned_data['pa']

            try:
             u=customer.objects.get(user=user)
             p=list(booking.objects.filter(user=u.id))
             if(pa==u.pa):
                return render(request,'Train/profile.html',{
                  'user':u ,'booking': p                              
               })   
               
            except Exception:
              p='Invalid Credantials'  
              return render(request,'Train/signin.html',{
                  'form':form , 'msg':p                                    
               }) 

        else:
            return render(request,'Train/signin.html',{
                'form':form
            })         


    return render(request,'Train/signin.html',{
        'form':newform()
    })    

def routes(request):
    return render(request,'Train/routes.html',{
         'station':station.objects.all()
    })    

def sign_up(request):
    if(request.method=='POST'):
        form=su_newform(request.POST)
        if(form.is_valid()):
             first=form.cleaned_data['first']
             user=form.cleaned_data['user']
             pa=form.cleaned_data['pa']
             dob=form.cleaned_data['dob']
             ge=form.cleaned_data.get('gender')
             ph=form.cleaned_data['ph']

             c=customer(first=first,user=user,pa=pa,dob=dob,g=ge,ph=ph)
             c.save()
             
        else:
            return render(request,'Train/signup.html',{
                'form':form
            })     


    return render(request,'Train/signup.html',{
          'form':su_newform()
    })    

def book(request):
    book=list(train.objects.all())
    if(request.method=='POST'):
            u=request.POST['user']
            p=request.POST['pass']
            t=request.POST['train']
            
            us=customer.objects.get(user=u)
            if(p==us.pa):
                 b=booking(user=us,trn=t) 
                 b.save()
                 return render(request,'Train/booking.html',{
                  'msg_1':'Booking completed Successfully','book':book
             })
                  
            else:
               return render(request,'Train/booking.html',{
                  'msg':u,'book':book
             })


            

    return render(request,'Train/booking.html',{
        'book':book
    })

def about(request):
    return render(request,'Train/about.html')    