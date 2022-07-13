from django.urls import path 
from .views import PostCreateView, PostDetailView
from . import views

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('logado/new/', PostCreateView.as_view(), name='post_new'),
    path('logado/', views.post_list, name='post_list')
]
