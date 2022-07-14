from pickle import GET
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


def post_list(request):
    posts = Post.objects.order_by('-date_posted')
    print(posts)
    return render(request, 'post/base.html', {
        "posts": posts
    })

class PostDetailView(DetailView): # new
    model = Post
    template_name = 'post/post_detail.html'

class PostCreateView(CreateView): # new
    model = Post
    template_name = 'post/post_new.html'
    fields = ['user','postagem', 'date_posted']

class PostDeleteView(DeleteView): # new
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('post_list')



