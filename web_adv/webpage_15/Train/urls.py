from unicodedata import name
from django.urls import path
from . import views

app_name='train'
urlpatterns=[
    path('',views.index,name='index'),
    path('signin/',views.sign_in,name='sign'),
    path('routes/',views.routes,name='routes'),
    path('signup/',views.sign_up,name='signup'),
    path('profile/',views.sign_in,name='profile'),
    path('booking/',views.book,name='booking'),
    path('about/',views.about,name='about')
]
