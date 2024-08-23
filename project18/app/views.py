from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    data = 'this is the data which i have sent from backend to front end'
    animal = "cat"
    c = 0
    date = datetime.now()
    d = {'data': data, "pet":animal, 'c':c, 'date':date}
    return render(request, 'home.html', d)


def display(request, mon):
    if mon == '1':
        month = 'January'
    elif mon == '2':
        month = 'i dont like'
    elif mon == '3':
        month = 'march'
    else:
        month = 'undefined month'
    d = {'month': month}
    return render(request, 'display.html', d)