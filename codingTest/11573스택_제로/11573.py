'''
N개의 정수들이 입력으로 주어진다.

첫번째 숫자 부터 순서대로 기록하다가, 중간에 0이 나오면 바로 이전에 입력된 숫자를 지운다.

0이 나올때 지울 숫자가 없는 경우는 없다.

최종적으로 기록된 숫자들의 총합을 계산하는 프로그램을 작성하자.

예를 들어, 4 0 2 3 0 이 입력되면 
[4]     # 4 기록
[]       # 0에 의해 4 삭제
[2]     # 2 기록
[2, 3]  # 3 기록
[2]     # 0에 의해 3 삭제

2만 기록된 상태이므로 합은 2가 된다.

반드시 스택을 활용해서 코드를 작성해보자.

입력>

첫 줄에 테스트 케이스 수가 주어진다.

각 테스트 케이스 마다 첫줄에 정수의 개수 N이 주어지고 (5 <= N <= 30)

다음 줄에 N개의 정수값(1이상 10이하)들이 공백으로 구분되어, 한 줄에 주어진다.

출력>
# 과 함께 테스트 케이스 번호를 출력하고, 최종적으로 적힌 수들의 합을 출력한다.
'''

'''
입력
3
5
4 0 2 3 0
5
10 0 10 0 3
7
9 2 0 0 8 0 8
'''

import sys; sys.stdin = open('sample_input.txt')

def my_push(data) :
    global top
    top += 1

    S[top] = data

def my_pop() :
    global top
    tmp = top
    top -= 1
    return S[tmp]

T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    S = [0] * N

    top = -1

    arr = list(map(int, input().split()))

    for num in arr :
        if num != 0 :
            try : 
                my_push(num)
            except: #top == N-1
                print('stack overflow')

        else :
            try :
                my_pop()
            except:
                print('nothing there')
    
    answer = sum(S[:top+1])
    print(f'#{tc} {answer}')

    
