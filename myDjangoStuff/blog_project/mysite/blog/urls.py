from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='list'),
    url(r'^about/',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='detail'),
    url(r'^post/new/$',views.CreateView,name='create'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.CreateView.as_view(),name='edit'),
    url(r'^post/(?P<pk>\d+)/remove/$',views.DeleteView.as_view(),name='remove'),
    url(r'^draft/$',views.DraftListView.as_view(),name='draft'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approval,name='comment_approval'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),

]
