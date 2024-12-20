import sys; sys.stdin = open('input.txt')

'''
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
'''
from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]

def bfs(r,c,d) :
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    q = deque()
    q.append((r,c,d))

    while q:
        vr, vc, vd = q.popleft()
        visited[vr][vc][vd] = 1

        if vr == N and vc == M :
            return
        
        for dr, dc in [[-1,0], [1,0], [0,-1], [0,1]] : #상 하 좌 우
            nr = vr + dr
            nc = vc + dc
            if 0<=nr<N and 0<=nc<M :
                


