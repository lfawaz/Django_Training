from django.shortcuts import render
from . import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.


class UserSignUp(CreateView):
        form = forms.CreateUsers
        template_name = 'signup'
        success_url = reverse_lazy('accounts/login.html')
