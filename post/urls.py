from django.urls import path
from .views import PostCreateView, PostDetailView, PostDeleteView
from . import views

urlpatterns = [
    path('logado/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('logado/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('logado/new/', PostCreateView.as_view(), name='post_new'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/new_post', views.tweet, name="new.post"),
    path('logado/<int:post_id>/comentarios', views.comentarios, name='view.comentario'),
    path('like/<int:pk>', views.LikeView, name="like_post"),
    path('perfil/', views.perfil, name='perfil'),
    path('alter/<id>', views.update_bio, name="update.profile")
]
