from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),

    #/todos/create_todo/
    path('create_todo/', views.create_todo, name = 'create_todo'),

    path('<str:work>/', views.detail, name = 'detail'),
]