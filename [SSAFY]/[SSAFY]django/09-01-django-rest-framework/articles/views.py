from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        #전체 게시글 조회(타입 : 쿼리셋) => 장고에서만 쓰는 데이터타입
        articles = Article.objects.all()
        # 변환하기 쉬운 포맷으로 전환 (직렬화)
        # 다중 데이터일때는 many=True 파라미터 주의
        serializer = ArticleListSerializer(articles, many=True) 
        return Response(serializer.data)
    
    elif request.method == 'POST' :
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #저장 성공 후 201 응답 상태 코드를 반환
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #유효성 검사 실패 후 400응답 상태코드를 반환
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#raise_exception
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        #전체 게시글 조회(타입 : 쿼리셋) => 장고에서만 쓰는 데이터타입
        articles = Article.objects.all()
        # 변환하기 쉬운 포맷으로 전환 (직렬화)
        # 다중 데이터일때는 many=True 파라미터 주의
        serializer = ArticleListSerializer(articles, many=True) 
        return Response(serializer.data)
    
    elif request.method == 'POST' :
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            #저장 성공 후 201 응답 상태 코드를 반환
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #유효성 검사 실패 후 400응답 상태코드를 반환
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    #단일 게시글 조회
    article = Article.objects.get(pk=article_pk)

    if reqeust.method=='GET':
    # 직렬화 진행
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT' :
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)