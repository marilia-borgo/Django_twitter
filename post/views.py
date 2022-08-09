from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# from django.template import context
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView
from GoogleNews import GoogleNews

from .forms import ProfileForm
from .models import Comentario, Post, Profile

googlenews = GoogleNews()
googlenews = GoogleNews(period='d')
googlenews = GoogleNews(lang='pt', region='BR')
googlenews.search('BRASIL')


def post_list(request):
    posts = Post.objects.order_by('-date_posted')
    comentarios = Comentario.objects.all()
    noticias = googlenews.results()
    return render(request, 'post/base.html', {
        "posts": posts,
        "comentarios": comentarios,
        "noticias": noticias
    })


def tweet(request):
    if request.method == "POST":
        new_tweet = request.POST["new_tweet"]
        Post.objects.create(user=request.user, postagem=new_tweet)
        return HttpResponseRedirect(reverse("post_list"))


def comentarios(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(pk=post_id)
        new_comment = request.POST["new_comment"]
        Comentario.objects.create(
            id_post_id=post.id, comentario=new_comment, user=request.user)
        return HttpResponseRedirect(reverse("post_list"))


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_list'))


def get_context_data(request, post_id):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    total_likes = post.total_likes()
    context = {"total_likes": total_likes}
    return context


class PostDetailView(DetailView):  # new
    model = Post
    template_name = 'post/post_detail.html'


class PostCreateView(CreateView):  # new
    model = Post
    template_name = 'post/post_new.html'
    fields = ['postagem']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostDeleteView(DeleteView):  # new
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('post_list')


def perfil(request):
    posts = Post.objects.order_by('-date_posted')
    comentarios = Comentario.objects.all()
    noticias = googlenews.results()
    bio = Profile.objects.all()
    return render(request, 'post/perfil.html', {
        "posts": posts,
        "comentarios": comentarios,
        "noticias": noticias,
        "bio": bio,

    })


def update_bio(request, id):
    obj = get_object_or_404(Profile, id=id)
    form = ProfileForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('perfil'))
    context = {"form": form}
    return render(request, "post/perfil_alter.html", context)
