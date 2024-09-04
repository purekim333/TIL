'''
오셀로라는 게임은 흑돌과 백돌을 가진 사람이 번갈아가며 보드에 돌을 놓아서 최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임이다.

보드는 4x4, 6x6, 8x8(가로, 세로 길이) 크기를 사용한다. 6x6 보드에서 게임을 할 때, 처음에 플레이어는 다음과 같이 돌을 놓고 시작한다(B : 흑돌, W : 백돌).

4x4, 8x8 보드에서도 동일하게 정가운데에 아래와 같이 배치하고 시작한다.



그리고 흑, 백이 번갈아가며 돌을 놓는다.

처음엔 흑부터 시작하는데 이 때 흑이 돌을 놓을 수 있는 곳은 다음과 같이 4군데이다.



플레이어는 빈공간에 돌을 놓을 수 있다.

단, 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 그 곳에 돌을 놓을 수 있고, 그 때의 상대편의 돌은 자신의 돌로 만들 수 있다.

(여기에서 "사이"란 가로/세로/대각선을 의미한다.)

(2, 3) 위치에 흑돌을 놓은 후의 보드는 다음과 같다.



이런 식으로 번갈아가며 흑, 백 플레이어가 돌을 놓는다.

만약 돌을 놓을 곳이 없다면 상대편 플레이어가 다시 돌을 놓는다.

보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임이 끝나고 그 때 보드에 있는 돌의 개수가 많은 플레이어가 승리하게 된다.


 [입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M이 주어진다. N은 4, 6, 8 중 하나이다.

그 다음 M줄에는 돌을 놓을 위치와 돌의 색이 주어진다.

돌의 색이 1이면 흑돌, 2이면 백돌이다.

만약 3 2 1이 입력된다면 (3, 2) 위치에 흑돌을 놓는 것을 의미한다.

돌을 놓을 수 없는 곳은 입력으로 주어지지 않는다.

 [출력]

각 테스트 케이스마다 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수를 출력한다.

흑돌이 30개, 백돌이 34인 경우 30 34를 출력한다.
'''

'''
입력
1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2
'''

import sys; sys.stdin = open('sample_input.txt')

# 돌을 놓으면 8방향 검사해서 다른 색의 돌이 나올떄까지 나머지 돌을 뒤집는 함수 작성
def osello(arr, x, y, dol) :
    s_x = y-1
    s_y = x-1
    arr[s_x][s_y] = dol  #먼저 돌 올려두고
    # print(x,y, s_x, s_y)
    for dr, dc in [[-1, 0], [1, 0] ,[0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]] : #상 하 좌 우 상대 우대 하대 좌대
        ni = s_x+dr
        nj = s_y+dc
        flip = []                                                                      # 8방향 검사하면서
        while 0<=ni<N and 0<=nj<N and arr[ni][nj] != dol and arr[ni][nj] != 0: # 같은 색 돌이 나올 떄 까지 그냥 바둑판이 나오기 전까지
            flip.append((ni, nj))
            ni += dr
            nj += dc
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == dol :
                for flip_x, flip_y in flip :
                    arr[flip_x][flip_y] = dol
    
    return arr                                                # 다른 놀이 나오면 뒤집자

T = int(input())

B = 1
W = 2

for tc in range(1, T+1) :
    N, M = map(int, input().split()) # 바둑판 개수, 돌을 놓는 횟수

     #초기 준비
    arr = [[0] * N for _ in range(N)]   #바둑판 만들기
    arr[N//2-1][N//2-1] = arr[N//2][N//2] = W    #처음 돌 4개 놓기 (N//2-1, N//2-1) ~ (N//2, N//2)
    arr[N//2-1][N//2] = arr[N//2][N//2-1] = B

    for _ in range(M) :
        x, y, dol = map(int, input().split()) #x, y 좌표 흑돌 : 1 / 백돌 : 2
        arr = osello(arr,x,y,dol)
        print()
        print(y-1, x-1, '에', dol, '돌 놓기')
        print()
        for row in arr :
            print(*row)

    w_count = 0
    b_count = 0
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] == B :
                b_count +=1 
            elif arr[i][j] == W :
                w_count += 1

    print(f'#{tc} {b_count} {w_count}')