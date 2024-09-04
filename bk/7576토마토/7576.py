import sys;sys.stdin = open('input.txt')

'''
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.



창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
'''
'''
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.
'''
from collections import deque

T = int(input())

def bfs(start_point) :
    #준비
    visited = [[0] * M for _ in range(N)]
    q = deque()
    for s_r, s_c in start_point :
        q.append((s_r, s_c))
        visited[s_r][s_c] = 1

    #탐색
    while q :
        v_r, v_c = q.popleft()
        for d_r, d_c in delta :
            n_r = v_r + d_r
            n_c = v_c + d_c
            if 0<=n_r<N and 0<=n_c<M and visited[n_r][n_c] == 0 and arr[n_r][n_c] == 0 :
                q.append((n_r, n_c))
                visited[n_r][n_c] = visited[v_r][v_c] + 1

    #완전 탐색이 끝났는데 
    for r in range(N) :
        for c in range(M) :
            if visited[r][c] == 0 and arr[r][c] != -1 : #방문하지 않았는데 벽이 아니면
                return -1
    
    else :
        return visited[v_r][v_c] -1 

for tc in range(1, T+1) :
    M, N = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]] #상 하 좌 우

    start_point = []
    for r in range(N) :
        for c in range(M) :
            if arr[r][c] == 1 :
                start_point.append([r,c])

    ans = bfs(start_point)



    print(ans)


