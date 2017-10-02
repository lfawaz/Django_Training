from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def index(response):
    return HttpResponse("<em>My Second App</em>")

def help(response):
    helpPageDict = {'help_page':'<em>This is my help page</em>'}
    return render(response,'AppTwo/help.html',helpPageDict)

def userList(request):
    user_list = User.objects.order_by('last_name')
    userDict = {'return_users': user_list}
    return render(request,'AppTwo/users.html', userDict)
