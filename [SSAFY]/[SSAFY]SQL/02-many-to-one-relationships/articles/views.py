from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_safe, require_POST, require_http_methods

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
@login_required
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        #왜래 키 데이터를 넣어야 함
        #인스턴스만 제공하고, 실제 저장은 잠시 보류
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article' : article,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def comments_delete(request, article_pk, comment_pk):
    #어떤 댓글을 삭제할지 조회
    comment = Comment.objects.get(pk=comment_pk)
    article = Article.objects.get(pk=article_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    #요청한 사용자 -> request.user
    #게시글 작성자 -> article.user
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/update.html', context)
    return redirect('articles:index')


@login_required
@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user :
        article.delete()
    return redirect('articles:index')
