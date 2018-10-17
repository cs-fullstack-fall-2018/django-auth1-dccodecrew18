from django.db import models
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class userModel(models.Model):
    user = models.CharField(max_length=50)
    blogtitle = models.CharField(max_length=100)
    blogentry = models.CharField(max_length=500)
    dateCreated =models.DateTimeField(default=datetime.now)
    #attributes below will be the link necessary  for user authenticty
    username = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.user, self.blogtitle,self.blogentry,self.dateCreated,self.username