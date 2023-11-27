from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # on delete : if the user account deleted then the post is also deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    # auto_now_add : add timestamp when post get created
    created_at = models.DateTimeField(auto_now_add=True)

    # auto_now :  whenever the post get updated it'll safe the timestamp
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title + "\n" + self.description

