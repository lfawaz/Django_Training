from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixins
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth import get_user_model

from view.generic import CreateView,ListView,DetailView,DetailView
from django.http import Http404

from braces.views import SelectRelatedMixin

from posts.models import Post
from django.contrib import messages

# Get User

User = get_user_model()

# Create your views here.

class PostListView(LoginRequiredMixins, SelectRelatedMixin, ListView):
    model = Post
    select_related = ['user','group']


class PostUserView(ListView):
    model = Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self,*args,**kwargs):
        try:
            self.post_user = User.objects.prefetchedrelated("posts").get(username__iexact=self.kwargs["username"])
        except User.DoesNotExit:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetailView(LoginRequiredMixins, SelectRelatedMixin, DetailView):
    model = Post
    select_related = ['user','group']

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(user__username__iexact=self.kwargs['username'])



class PostCreateView(LoginRequiredMixins, SelectRelatedMixin, CreateView):
    fields = ('message','group')
    model = Post
    select_related = ['user','group']

    def form_valid(self, form):
        self.obect = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixins, SelectRelatedMixin, DeleteView):
    model = Post
    select_related = ['user','group']
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(user_id=self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,"Post Deleted")
        return super().delete(*args,**kwargs)
