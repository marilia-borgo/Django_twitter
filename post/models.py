from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    postagem = models.TextField(null=True, blank=True)
    created =  models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.postagem

