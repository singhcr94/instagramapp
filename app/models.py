from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.
from django.db import models


class profilelist(models.Model):
    following=models.ForeignKey(User,related_name="following",on_delete=models.SET_NULL,null=True)
    followers=models.ForeignKey(User,related_name="followers", on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.following.username

class image(models.Model):
    user=models.ForeignKey(User,related_name='user',on_delete=models.SET_NULL,null=True)
    profilepic=models.ImageField(upload_to='profilepic',null=True,blank=True,unique=True)
    postpics=models.ImageField(upload_to='postpic',null=True,blank=True)
    def __str__(self):
        return self.user.username


