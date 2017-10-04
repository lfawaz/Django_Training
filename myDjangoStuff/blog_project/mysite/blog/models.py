from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.

class Post(models.Model):

    author = models.ForeignKey('auth.User')
    title  = models.CharField(max_length=200)
    text   = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField()

    def publish(self):
        published_date = timezone.now()
        self.save()

    def approved_comments(self):
        Comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Post_Detail',kwargs{'pk':self.pk})

class Comment(models.Model):
    post = ForeignKey('blog.Post',related_name=Comment)
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('Post_List')
