from django.urls import path 
# from .views import PostagemList
from . import views
urlpatterns = [
    # path('', PostagemList.as_view(), name='postagens'),
    path('logado/', views.post_list, name='post_list')
]
