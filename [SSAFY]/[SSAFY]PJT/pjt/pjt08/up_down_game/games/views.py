from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from .models import GameSession

import random

# Create your views here.
def start_game(request):
    target_number = random.randint(1, 100)
    game_session = GameSession.objects.create(target_number=target_number)
    context = {
        'target_number' : target_number,
        'game_session_id': game_session.id,
    }

    return render(request, 'games/game.html', context)

#사용자의 추측 번호를 전달 받을 것
def make_guess(request, game_session_id):
    game_session = get_object_or_404(GameSession, id=game_session_id)
    if request.method == 'POST' :
        user_guess = int(request.POST.get('user_guess'))

        message = ''
        if user_guess < 1 or user_guess > 100 :
            message = '1~100 사이 숫자만 입력하세요.'
        elif user_guess > game_session.target_number :
            message = 'DOWN!'
            game_session.user_guess = user_guess
            game_session.attempts += 1
            game_session.save()
        elif user_guess < game_session.target_number:
            message = 'UP!'
            game_session.user_guess = user_guess
            game_session.attempts += 1
            game_session.save()
        else :
            message = '정답입니다!'
            game_session.attempts += 1
            game_session.save()

        response_data = {
            'message' : message,
            'attempts' : game_session.attempts,
        }
        return JsonResponse(response_data)
    else :
        return JsonResponse({'error' : 'Invalid HTTP Request'})