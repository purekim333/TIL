'''
동전처럼 생긴 돌의 양면은 각각 흰색과 검은색으로 되어있고, 게임의 규칙은 다음과 같다.

i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해, 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.
주어진 돌을 벗어나는 경우 뒤집기는 중지된다.

[입력]
첫 줄에 게임의 개수 T, 다음 줄부터 게임별로 첫 줄에 N, M, 다음 줄에 N개 돌의 초기상태, 이후 M개의 줄에 걸쳐 i, j가 주어진다.
(1<=T<=50, 3<=N<=20,   1<=M<=10, 1<=i, j<=N)

[출력]
#과 게임번호, 빈칸에 이어 빈칸으로 구분된 돌의 상태를 출력한다.
'''
'''입력
3
5 1
0 1 0 1 0
2 2
5 1
0 1 0 0 0
2 3
10 4
0 1 1 0 0 1 0 1 0 1
3 2
5 3
4 4
8 4
'''

import sys; sys.stdin = open('sample_in.txt')

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    i_lst = []
    j_lst = []

    for _ in range(M) :
        i, j = map(int, input().split())
        i_lst.append(i-1)
        j_lst.append(j+1)

    for k in range(M) :
        standard = i_lst[k]
        for step in range(1, j_lst[k]):
            left = standard - step
            right = standard + step
            if 0<= left < N and 0 <= right < N :
                if arr[left] == arr[right] :
                    arr[left] = int(not arr[left])
                    arr[right] = int(not arr[right])
                else :
                    pass
    
    print(f'#{tc}', *arr)
                



