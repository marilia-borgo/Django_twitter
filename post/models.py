import base64
import sys
from distutils.command import upload

from django import dispatch
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    postagem = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='twitter_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.postagem}"

    def get_absolute_url(self):
        return reverse('post_list')


class Comentario(models.Model):
    id_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, blank=True)
    comentario = models.CharField(max_length=180, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comentarios', null=True, blank=True)

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('post_list')


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.DO_NOTHING, related_name="profile")
    foto = models.ImageField(upload_to='profile/fotos')
    bio = models.TextField(null=True, blank=True)
    capa = models.URLField(null=True)
    image64 = models.TextField(null=True, blank=True)


@receiver(post_save, sender=Profile)
def to_base64(sender, instance, **kwargs):
    with open('/home/lucassilva/Twitter-clone/Django_twitter/'+instance.foto.url, "rb") as image:
        b64_string = base64.b64encode(image.read())

    instance.image64 = b64_string.decode('utf-8')

    post_save.disconnect(to_base64, sender=Profile)
    instance.save(update_fields=['image64'])
    post_save.connect(to_base64, sender=Profile)
