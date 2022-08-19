from django.urls import path
from . import views

app_name='page3'
urlpatterns=[
    path("", views.index, name="index"),
    path("add/",views.add,name="add")
]