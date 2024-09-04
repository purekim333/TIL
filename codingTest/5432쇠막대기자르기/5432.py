'''
여러 개의 쇠막대기를 레이저로 절단하려고 한다.

효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다.

쇠막대기와 레이저의 배치는 다음 조건을 만족한다.

 - 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.

 - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.

 - 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.

 - 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

아래 그림은 위 조건을 만족하는 예를 보여준다.

수평으로 그려진 굵은 실선은 쇠막대기이고, 점은 레이저의 위치, 수직으로 그려진 점선 화살표는 레이저의 발사 방향이다.

 

이러한 레이저와 쇠막대기의 배치는 다음과 같이 괄호를 이용하여 왼쪽부터 순서대로 표현할 수 있다.

    1. 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 “()” 으로 표현된다. 또한, 모든 “()”는 반드시 레이저를 표현한다.

    2. 쇠막대기의 왼쪽 끝은 여는 괄호 ‘(’ 로, 오른쪽 끝은 닫힌 괄호 ‘)’ 로 표현된다.

위 예의 괄호 표현은 그림 위에 주어져 있다.

쇠막대기는 레이저에 의해 몇 개의 조각으로 잘려지는데, 위 예에서 가장 위에 있는 두 개의 쇠막대기는 각각 3개와 2개의 조각으로 잘려지고,

이와 같은 방식으로 주어진 쇠막대기들은 총 17개의 조각으로 잘려진다.

쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램을 작성하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의 개수는 최대 100,000이다.

[출력]

각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 잘려진 조각의 총 개수를 출력한다.
'''

'''
입력
2
()(((()())(())()))(())
(((()(()()))(())()))(()())	//전체 TC 개수
//첫 번째 TC
//두 번째 TC
'''

import sys; sys.stdin = open('sample_input.txt')

def my_push(data) :
    global top
    top += 1
    stack[top] = data

def my_pop() :
    global top
    tmp = top
    top -= 1
    return stack[tmp] 

T = int(input())

for tc in range(1, T+1):
    arr = input()

    stack = [0] * len(arr)
    top = -1

    #아이디어
    # push 바로 뒤에 pop이 나오면 레이저
        # 어떻게 확인하지 
        # 1) top과 idx 비교?
        # 2) 이전에 했던 결과 비교 -> flag 변수
    # 아니라면 stick
    is_push = True
    total_cnt = 0
    for i in range(len(arr)) :
        if arr[i] == '(' :
            my_push(i)
            is_push = True
        else : # ')'
            data = my_pop()
            if is_push : #이전에 푸쉬가 있었다면
                total_cnt += top + 1
            else : #이전에 푸쉬가 없었다면
                total_cnt += 1
                
            is_push = False

    print(f'#{tc}', total_cnt)

    # total_cnt = 0
    # for tick in stick :
    #     start, end = tick
    #     stick_cnt = 1
    #     for point in laser :
    #         if start < point < end :
    #             stick_cnt += 1 
    #     total_cnt += stick_cnt
    # print('stick', stick)
    # print('laser', laser)

    # total_cnt = 0
    # for i in range(len(arr)) :
    #     if arr[i] == '(' :
    #         my_push(i)
    #         is_push = True
    #     else : # ')'
    #         data = my_pop()
    #         if top == -1 :
    #             laser_cnt = 0
                
    #         elif is_push : #이전에 푸쉬가 있었다면
    #             laser_cnt += 1
    #         else : #이전에 푸쉬가 없었다면
    #             laser_cnt = 0
    #             for point in laser :
    #                 if data < point < i :
    #                     laser_cnt += 1

    #             total_cnt += laser_cnt + 1
                
    #         is_push = False

    


        



