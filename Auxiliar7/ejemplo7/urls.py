from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('cursos/', views.cursos, name='cursos'),
    path('users/', views.users, name='users'),
    path('adduser/', views.adduser, name='adduser'),
    path('added/', views.added, name='added'),
 ]
