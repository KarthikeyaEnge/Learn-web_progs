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
        return f"train {self.id} : {self.origin} to {self.destination} duration {self.duration} "