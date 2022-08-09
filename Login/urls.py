from django.urls import path
from Login.views.index import IndexView
from Login.views.signup import SignupView
from Login.views.login import LoginView
from Login.views.logout import LogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
