from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request) :
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)
    
def detail(request, article_pk) :
    article = Article.objects.get(pk = article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)
    
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST['title']
    content = request.POST['content']
    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:detail', article.pk)
    # return redirect(f'/articles/{article.pk}')

def delete(request, article_pk):
    if request.method == 'POST' :
        article = Article.objects.get(pk=article_pk)
        article.delete()
    return redirect('articles:index')

def edit(request, article_pk):
    
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    article.title = request.POST['title']
    article.content = request.POST.get('content')

    article.save()
    return redirect('articles:detail', article.pk)