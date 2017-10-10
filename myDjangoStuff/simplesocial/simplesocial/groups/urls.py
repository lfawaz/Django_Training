from django.conf.urls import url
from . import views

app_name = 'groups'

urlpattern=[
    url(r'^$',views.GroupListView.as_view(),name='all'),
    url(r'^create/$',views.GroupCreateView.as_view(),name='create'),
    url(r'^posts/in/(?P<slug>[-\w]+)/$',views.GroupDetailView.as_view,name='detail'),
]
