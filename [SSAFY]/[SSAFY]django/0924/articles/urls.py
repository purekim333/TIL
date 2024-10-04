from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),

    #게시글 작성
    #1. 폼 요청 => get new
    path('new/', views.new, name='new'),
    #2. 레코드 생성 => post create
    path('create/', views.create, name='create'),

    #게시글 삭제
    #POST /articles/<int:article_pk>/delete/
    path('<int:article_pk>/delete/', views.delete, name='delete'),

    #게시글 수정
    # 수정폼 요청 => GET /articles/<int:aritcle_pk>/edit/
    path('<int:article_pk>/edit/', views.edit, name = 'edit'),
    # 레코드 수정 => POST /articles/<int:article_pk>/update/
    path('<int:article_pk>/update/', views.update, name='update'),

]
