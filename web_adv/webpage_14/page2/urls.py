from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name='index'),
    path("isityogaday/",views.isityogaday,name='yoga'),
    path("evendate/",views.evendate,name='evendate')
]