from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

def post_list(request):
    posts = Post.objects.all()
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
    fields = '__all__'

class PostDeleteView(DeleteView): # new
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('post_list')