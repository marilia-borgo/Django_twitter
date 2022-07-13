from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Post

# Create your views here.


# class PostagemList(DetailView):
#     model = Post
#     context_object_name = 'posts'
#     template_name = 'post/base.html'

def post_list(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'post/base.html', {
        "posts": posts
    })
