from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="index"),
    path('register', views.register, name="register"),
    path('success', views.success, name="success"),
    path('login', views.login, name="login"),
    path('index', views.task,name="index"),
    path('add', views.add, name="add"),
    path('saved', views.saved, name="saved"),
    path('show', views.show, name="show"),
    path('search', views.search, name="search"),
    path('result', views.result, name="result"),

]
