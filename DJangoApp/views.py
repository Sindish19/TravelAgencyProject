from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from DJangoApp.models import Kontakt, Tours, FavTours


def save_message(request):
    first_name=request.POST['name']
    last_name=request.POST['lname']
    email=request.POST['email']
    message=request.POST['comments']
    telefon=request.POST['tel']
    select=request.POST['zgjidh']


    Kontakt(
        first_name=first_name,
        last_name=last_name,
        email=email,
        message=message,
        tel=telefon,
        select=select
    ).save()

    return HttpResponseRedirect('/')

def index(request):
    tours=Tours.objects.all()
    favtours=FavTours.objects.all()
    return render(request, 'webpage.html',{'tours':tours, 'favtours': favtours})

def aboutus(request):
    return render(request, 'aboutus.html')



