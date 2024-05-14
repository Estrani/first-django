from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Ad


def hello(request):
    bands = Band.objects.all()
    return render(request,
                    'listings/hello.html',
                    {'bands': bands})




def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def contact(request):
    return render(request,
                    'listings/contact.html')

def listings(request):
    ads = Ad.objects.all()
    return render(request,
                    'listings/listings.html',
                    {'ads': ads})
