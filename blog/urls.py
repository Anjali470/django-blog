from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('home', views.home, name='home'),
    path('newpost', views.newpost, name='newpost'),
    path('mypost', views.myposts, name='myposts'),
    path('logout', views.logout, name='logout')
]