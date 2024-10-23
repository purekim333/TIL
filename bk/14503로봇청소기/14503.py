import sys; sys.stdin = open('input.txt')

'''
로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 방은 
$N \times M$ 크기의 직사각형으로 나타낼 수 있으며, 
$1 \times 1$ 크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북 중 하나이다. 방의 각 칸은 좌표 
$(r, c)$로 나타낼 수 있고, 가장 북쪽 줄의 가장 서쪽 칸의 좌표가 
$(0, 0)$, 가장 남쪽 줄의 가장 동쪽 칸의 좌표가 
$(N-1, M-1)$이다. 즉, 좌표 
$(r, c)$는 북쪽에서 
$(r+1)$번째에 있는 줄의 서쪽에서 
$(c+1)$번째 칸을 가리킨다. 처음에 빈 칸은 전부 청소되지 않은 상태이다.

로봇 청소기는 다음과 같이 작동한다.

현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
현재 칸의 주변 
$4$칸 중 청소되지 않은 빈 칸이 없는 경우,
바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
현재 칸의 주변 
$4$칸 중 청소되지 않은 빈 칸이 있는 경우,
반시계 방향으로 
$90^\circ$ 회전한다.
바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
1번으로 돌아간다.
'''
from collections import deque

direction = [[-1,0], [0,1], [1,0], [0,-1]]

def chk_clean(v_r, v_c, visited):
    for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]] : #위 왼 아래 오
        nr = v_r + dr
        nc = v_c + dc
        if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and arr[nr][nc] == 0: #청소 가능하면
            return True
        else :
            return False

def bfs(r, c, d, arr):
    visited = [[0] * M for _ in range(N)]
    v_r, v_c = r, c
    v_d = d
    q = deque()
    q.append(v_r, v_c, v_d)

    while q:
        v_r, v_c, v_d = q.popleft()
        visited[v_r][v_c] = 1

        for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]] : #위 왼 아래 오
            nr = v_r + dr
            nc = v_c + dc
            if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0 and arr[nr][nc] == 0: #벽이 아니라면
                
                nd = (v_d + 3) % 4 #반시계 회전
                move_r, move_c = direction[nd]
                next_r = v_r + move_r
                next_c = v_c + move_c
                if 0<=next_r<N and 0<=next_c<M and visited[next_r][next_c] == 0 and arr[next_r][next_c] == 0:
                    q.append(next_r, next_c, nd)
                else :

T = int(input())

for tc in range(1, T+1):
    N , M = map(int, input().split())
    r, c, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
