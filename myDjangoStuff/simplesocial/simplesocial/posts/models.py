from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.urlresolvers import reverse
from django.conf import settings

import misaka

from groups.models import Group

# Create your models here.

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts")
    group = models.ForeignKey(Group, related_name="posts")
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField(max_lenght=500)
    message_html = models.TextField(editable=False)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username': self.user.username,'pk':self.pk})

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user","group"]
