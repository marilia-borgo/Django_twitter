from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import Post

# Create your views here.


# class PostagemList(ListView):
#     model = Post
#     template_name = 'post/base.html'
#     # template_name = 'post/base.html'

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