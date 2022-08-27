from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from tkinter import CASCADE
from tkinter.simpledialog import SimpleDialog
from types import CoroutineType
from django.db import models

# Create your models here.
class station(models.Model):
    sid=models.CharField(max_length=10)
    city=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.sid}:{self.city}"



class train(models.Model):
    origin=models.ForeignKey(station,on_delete=models.CASCADE,related_name='departures')
    destination=models.ForeignKey(station,on_delete=models.CASCADE,related_name='arrivals')
    duration=models.IntegerField()

    def __str__(self):
        return f"train {self.id} : {self.origin} to {self.destination} duration {self.duration} Mins"


class customer(models.Model):
    first=models.CharField(max_length=64)
    user=models.CharField(max_length=64,unique=True)
    pa=models.CharField(max_length=8,unique=True)
    dob=models.DateField()
    g=models.CharField(max_length=10)
    ph=models.IntegerField(unique=True)  

    def __str__(self):
        return f"username:{self.user}"     


class booking(models.Model):
    user=models.ForeignKey(customer,on_delete=models.CASCADE,related_name='customer')
    trn=models.CharField(max_length=64)

    def __str__(self):
        return f"Passenger : {self.user} Train : {self.trn}"