from django.shortcuts import render
from django.generic.views import CreateView, DetailView, ListView

from django.contrib.auth.mixins import LoginRequiredMixins, PermissionsRequiredMixin
from django.core.urlresolvers import reverse
from groups.models import Group
# Create your views here.

class GroupCreateView(CreateView):
    fields = ('name','description')
    model = Group

class GroupDetailView(DetailView):
    model = Group

class GroupListView(ListView):
    model = Group
