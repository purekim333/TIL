from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    # if request.method == 'POST' :
    form = ArticleForm(request.POST)
    if form.is_valid() :
        article = form.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {
        'form' : form,
        }
        return render(request, 'articles/create.html', context)

        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()
        return redirect('articles:index')
    
    # else:
    #     form = ArticleForm()
    #     context = {
    #         'form' : form,
    #     }
    #     return render(request, 'articles/create.html', context)
    
# def create(request):
# if request.method == 'POST' :
#     form = ArticleForm(request.POST)
#     if form.is_valid() :
#         article = form.save()
#         return redirect('articles:detail', article.pk)
#     else:
#         context = {
#         'form' : form,
#         }
#         return render(request, 'articles/create.html', context)

#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # article = Article(title=title, content=content)
#     # article.save()
#     return redirect('articles:index')

# else:
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/create.html', context)

def update(request, article_pk):
    if request.method == 'POST':
        article=Article.objects.get(pk=article_pk)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid() :
            article = form.save()
            return redirect('articles:detail', article.pk)
    else :
        article = Article.objects.get(pk=article_pk)
        form = ArticleForm(instance=article)
        
        context = {
            'article' : article,
            'form' : form,
        }
        return render(request, 'articles/update.html', context)
