from django.shortcuts import render

# Create your views here.
def index(request):
    mydict = {'this_request': 'testing my second app'}
    return render(request,'second_app/index.html',context=mydict)
