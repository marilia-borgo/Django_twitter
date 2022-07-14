from django.urls import path 
from .views import PostCreateView, PostDetailView, PostDeleteView
from . import views

urlpatterns = [
    path('logado/<int:pk>/delete/',PostDeleteView.as_view(), name='post_delete'),
    path('logado/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('logado/new/', PostCreateView.as_view(), name='post_new'),
    path('logado/', views.post_list, name='post_list')
]
