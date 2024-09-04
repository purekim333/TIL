'''
NxN 크기의 미로에서 출발지 목적지가 주어진다.

이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.

경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100

0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

'''입력
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
'''

import sys; sys.stdin = open('sample_input.txt')
from collections import deque

def find_start(maze, N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


def bfs(maze, N, start_x, start_y):
    dr = [-1, 1, 0, 0]  # 상 / 하 / 좌/ 우
    dc = [0, 0, -1, 1]  # 상 / 하 / 좌/ 우

    # 준비
    visited = [[0] * (N) for _ in range(N)]  # visited 생성
    D = [[0] * (N) for _ in range(N)]  # 거리 측정 배열 생성
    P = [[0] * (N) for _ in range(N)]  # P 배열 생성
    Q = deque()  # Q생성
    Q.append((start_x, start_y))  # 시작점 Q에 삽입
    visited[start_x][start_y] = 1  # visited에 표시

    # 탐색
    while Q:  # q가 빌때까지
        v_x, v_y = Q.popleft()  # deque
        if maze[v_x][v_y] == 3: # 결과 확인
            return D[v_x][v_y] - 1
        for i in range(4):
            di = v_x + dr[i]  # 갈 수 있는 곳 선정
            dj = v_y + dc[i]
            if 0 <= di < N and 0 <= dj < N and maze[di][dj] != 1 and visited[di][dj] == 0:
                Q.append((di, dj))  # Q에 삽입
                visited[di][dj] = 1 # visitied 기록
                D[di][dj] = D[v_x][v_y] + 1 # 거리 기록
                P[di][dj] = (v_x, v_y)      # 이전 위치 기록

    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]

    start_x, start_y = find_start(maze, N)

    ans = bfs(maze, N, start_x, start_y)

    print(f'#{tc} {ans}')

