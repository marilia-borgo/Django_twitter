from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView
from .models import Comentario, Post
from django.urls import reverse_lazy



def post_list(request):
    posts = Post.objects.order_by('-date_posted')
    comentarios = Comentario.objects.all()
    return render(request, 'post/base.html', {
        "posts": posts,
        "comentarios": comentarios,
    })

class PostDetailView(DetailView): # new
    model = Post
    template_name = 'post/post_detail.html'
    
class PostCreateView(CreateView): # new
    model = Post
    template_name = 'post/post_new.html'
    fields = ['postagem']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)

class PostDeleteView(DeleteView): # new
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('post_list')



