from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo import forms

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

def userSignUpForm(request):
    form = forms.SignUpForm()

    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return userList(request)

    return render(request,'AppTwo/signup.html',{'form': form})
