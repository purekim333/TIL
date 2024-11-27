from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse
from django.core.paginator import Paginator
from django.conf import settings
import requests, openai

@api_view(['GET'])
def exchange(request, fromCountry, price):
    # 환율 정보 가져오기
    API_KEY = settings.CURRENCY_API_KEY
    URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&data=AP01'
    requestData = requests.get(URL)
    todayresult = requestData.json()

    exchange_rate= 1
    exchangeresult= 1

    # 환율 계산
    for data in todayresult:
        if data.get('cur_unit') == fromCountry:
            exchange_rate = float(data.get('deal_bas_r').replace(',',''))
            exchangeresult = price * exchange_rate
            break
    return Response({"exchangeresult": exchangeresult})

@api_view(['GET'])
def exchange_foreign(request, fromCountry, price):
    # 환율 정보 가져오기
    API_KEY = settings.CURRENCY_API_KEY
    URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&data=AP01'
    requestData = requests.get(URL)
    todayresult = requestData.json()

    exchange_rate= 1
    exchangeresult= 1

    # 환율 계산
    for data in todayresult:
        if data.get('cur_unit') == fromCountry:
            exchange_rate = float(data.get('deal_bas_r').replace(',',''))
            exchangeresult = price * (1/exchange_rate)
            break
    return Response({"exchangeresult": exchangeresult})

# 뉴스
def news(request):
    query = '경제'
    display_count = 100
    page = int(request.GET.get('page', 1))
    
    url = 'https://openapi.naver.com/v1/search/news.json'
    headers = {
        'X-Naver-Client-Id': settings.NAVER_CLIENT_ID,
        'X-Naver-Client-Secret': settings.NAVER_CLIENT_SECRET,
    }
    params = {
        'query': query,
        'display': display_count,
        'start': (page - 1) * 10 + 1,  # 페이지 시작 번호
        'sort': 'date',
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return JsonResponse({'error': '네이버 API 호출 실패'}, status=response.status_code)

    news_data = response.json().get('items', [])
    
    # 페이지네이션
    paginator = Paginator(news_data, 10)  # 한 페이지당 10개
    current_page_data = paginator.get_page(page)

    return JsonResponse({
        'news': list(current_page_data),
        'total_pages': paginator.num_pages,
        'current_page': current_page_data.number,
    }, safe=False)

# 챗봇 기능
@api_view(['POST'])
def chat_with_gpt(request):
    user_message = request.data.get('message', '').strip()
    if not user_message:
        return Response({'error': '메시지를 입력해주세요.'}, status=status.HTTP_400_BAD_REQUEST)

    openai.api_key = settings.OPENAI_API_KEY

    try:
        # OpenAI API 호출
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # 모델 이름 확인
            messages=[
                {"role": "system", "content": "You are the famous rapper. You are a helpful assistant. You always answer with the rhyme."},
                {"role": "user", "content": user_message},
            ],
        )
        reply = response['choices'][0]['message']['content']
        return Response({'reply': reply}, status=status.HTTP_200_OK)
    except Exception as e:  # 모든 예외를 처리
        print(f"OpenAI API 호출 오류: {e}")
        return Response({'error': f'OpenAI API 호출 오류: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# # 키 확인하기
# def call_openai_api(user_message):
#     """
#     OpenAI API 호출 함수
#     """
#     openai.api_key = settings.OPENAI_API_KEY

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",  # 모델 이름을 최신 버전에 맞게 수정
#             messages=[
#                 {"role": "system", "content": "You are the famous rapper. You are a helpful assistant. You always answer with the rhyme."},
#                 {"role": "user", "content": user_message},
#             ],
#         )
#         return response['choices'][0]['message']['content']
#     except Exception as e:
#         raise RuntimeError(f"OpenAI API 호출 오류: {e}")

# @api_view(['POST'])
# def chat_with_gpt(request):
#     user_message = request.data.get('message', '').strip()
#     if not user_message:
#         return Response({'error': '메시지를 입력해주세요.'}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         reply = call_openai_api(user_message)
#         return Response({'reply': reply}, status=status.HTTP_200_OK)
#     except RuntimeError as e:
#         print(str(e))
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
