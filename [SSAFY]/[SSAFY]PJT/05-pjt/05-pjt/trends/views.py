from django.shortcuts import render, redirect
from .models import Keyword, Trend
import re
import os
from django.conf import settings

from bs4 import BeautifulSoup
from selenium import webdriver

def get_google_data(keyword):
    url = f"https://www.google.com/search?q={keyword}"
    # 크롬 브라우저가 열린다. 이 때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source 
    soup = BeautifulSoup(html, "html.parser")

    result = soup.select_one('#result-stats').text

    return result

def get_advanced_data(keyword):
    url = f"https://www.google.com/search?q={keyword}&tbs=qdr:y"
    # 크롬 브라우저가 열린다. 이 때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source 
    soup = BeautifulSoup(html, "html.parser")

    result = soup.select_one('#result-stats').text

    return result


# Create your views here.
def keyword(request):
    if request.method == 'POST' :
        keyword = Keyword(name=request.POST.get('keyword'))
        keyword.save()
        return redirect('trends:keyword')
    else :
        keywords = Keyword.objects.all()
    context = {
        'keywords' : keywords,
    }
    return render(request, 'trends/keyword.html', context)

def delete(request, keyword_pk):
    if request.method == 'POST':
        keyword = Keyword.objects.get(pk=keyword_pk)
        keyword.delete()
    return redirect('trends:keyword')

def crawling(request):
    querylist = []
    querySets = Keyword.objects.all().values('name')
    for querySet in querySets:
        querylist.append(querySet['name'])
    for query in querylist:
        text = get_google_data(query)
        result = int(re.findall(r"[\d,]+", text)[0].replace(',', ''))
        trend, created_trend = Trend.objects.get_or_create(name=query, result=result, search_period='all')
    context = {
        'trends' : Trend.objects.all(),
    }
    return render(request, 'trends/crawling.html', context)



import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

import base64   # 텍스트 <-> 이진 데이터 변환 모듈
from io import BytesIO   # 메모리 내에서 이진 데이터를 파일처럼 다룰 수 있게 해주는 모듈

def histogram(request):
    querylist = []
    valuelist = []
    querySets = Trend.objects.all().values('name', 'result')
    for querySet in querySets:
        querylist.append(querySet['name'])
        valuelist.append(querySet['result'])

    labels = querylist
    values = valuelist
    
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='skyblue')

    # 그래프 제목 및 레이블 추가
    plt.xlabel('Keyword', fontsize=12)
    plt.ylabel('Search Results', fontsize=12)
  
    # 그래프 이미지를 임시로 저장할 버퍼 생성
    buffer = BytesIO()
    # 그래프를 버퍼에 저장. 이미지 형식은 png로 설정
    plt.savefig(buffer, format='png')
    # 버퍼의 내용을 base64로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        # 저장된 이미지의 경로로 저장
        'chart_image': f'data:image/png;base64, {image_base64}',
    }

    return render(request, 'trends/crawling_histogram.html', context)



    # return render(request, 'trends/crawling_histogram.html')

def advanced(request):
    querylist = []
    querySets = Keyword.objects.all().values('name')
    for querySet in querySets:
        querylist.append(querySet['name'])
    for query in querylist:
        text = get_advanced_data(query)
        result = int(re.findall(r"[\d,]+", text)[0].replace(',', ''))
        trend, created_trend = Trend.objects.get_or_create(name=query, result=result, search_period='year')
   
   
    querylist = []
    valuelist = []
    querySets = Trend.objects.filter(search_period='year').values('name', 'result')
    for querySet in querySets:
        querylist.append(querySet['name'])
        valuelist.append(querySet['result'])

    labels = querylist
    values = valuelist
    
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='skyblue')

    # 그래프 제목 및 레이블 추가
    plt.xlabel('Keyword', fontsize=12)
    plt.ylabel('Search Results', fontsize=12)
  
    # 그래프 이미지를 임시로 저장할 버퍼 생성
    buffer = BytesIO()
    # 그래프를 버퍼에 저장. 이미지 형식은 png로 설정
    plt.savefig(buffer, format='png')
    # 버퍼의 내용을 base64로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        # 저장된 이미지의 경로로 저장
        'chart_image': f'data:image/png;base64, {image_base64}',
    }

    return render(request, 'trends/crawling_histogram.html', context)