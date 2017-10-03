from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from basic_app.models import School,Student
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'basic_app/school_details.html'

class SchoolCreateView(CreateView):
    model = School
    fields = ('name','princpal','location')

class SchoolUpdateView(UpdateView):
    model = School
    fields = ('name','princpal')

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('basic_app:list')
