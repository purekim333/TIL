from django.shortcuts import render, redirect
# 모델 클래스 가져오기
from .models import Article

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def news(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    #저장1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #저장2
    article = Article(title=title, content=content)
    article.save()
    #유효셩 검사를 위해 2번 저장 방법을 사용함!

    # #저장3
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)

def delete(request, pk):
    article = Article.objects.get(pk=pk)

    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 어떤 게시글 수정할지 조회
    article = Article.objects.get(pk=pk)
    # 사용자로부터 받은 새로운 입력 데이터 추출
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 기존 게시글의 데이터를 사용자로 받은 데이터로 새로 할당
    article.title = title
    article.content = content
    # 저장
    article.save()

    return redirect('articles:detail', article.pk)