from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from blog.models import Post
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixins
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm
from django.urls import reverse_lazy
from blog.models import Post,Comment


class AboutView(TemplateView):
    name = 'about.html'


class PostListView(ListView):
    model = Posta

    def get_queryset(self):
        return Post.object.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixins,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class PostUpdateView(LoginRequiredMixins,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class PostDeleteView(LoginRequiredMixins,DeleteView):
    login_url = 'login'
    model = Post
    success_url = reverse_lazy('blog/post_detail.html')

class DraftListView(LoginRequiredMixins,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post

    def get_queryset(self):
        return Post.object.filter(published_date__isnull=True).order_by('-created_date')


#################################################
#Function views
################################################

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method = 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(request,'post_detail',pk=post.pk)
    else:
        form = CommentForm()

    return render(request,'blog/comment_form.html',{'form':form})


@login_required
def comment_approval(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()

    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = Comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
