from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('display<mon>', display, name='display')
]
