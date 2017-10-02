from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    mydict = {'insert_me': 'I am coming from views.html'}
    return render(response,'first_app/index.html',mydict)
