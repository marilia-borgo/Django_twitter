from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    postagem = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return f"{self.postagem}"

    def get_absolute_url(self): 
        return reverse('post_list')

class Comentario(models.Model):
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comentario = models.CharField(max_length=180, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comentarios', null=True, blank=True)

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('post_list')
    
