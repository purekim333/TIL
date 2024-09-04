import sys; sys.stdin = open('input.txt')

from collections import deque

def bfs(start_point) :
    #준비
    visited = [[[0] * M for _ in range(N)] for _ in range(H)]
    q = deque()
    for s_r, s_c, s_h in start_point :
        q.append((s_r, s_c, s_h))
        visited[s_h][s_r][s_c] = 1

    #탐색
    while q :
        v_r, v_c, v_h = q.popleft()
        for d_r, d_c, d_h in delta :
            n_r = v_r + d_r
            n_c = v_c + d_c
            n_h = v_h + d_h
            if 0<=n_r<N and 0<=n_c<M and 0<=n_h<H and visited[n_h][n_r][n_c] == 0 and arr[n_h][n_r][n_c] == 0 :
                q.append((n_r, n_c, n_h))
                visited[n_h][n_r][n_c] = visited[v_h][v_r][v_c] + 1

    #완전 탐색이 끝났는데
    for h in range(H) : 
        for r in range(N) :
            for c in range(M) :
                if visited[h][r][c] == 0 and arr[h][r][c] != -1 : #방문하지 않았는데 벽이 아니면
                    return -1
    
    else :
        return visited[v_h][v_r][v_c] -1

T = int(input())

for tc in range(1, T+1):
    M, N , H = map(int, input().split())

    arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

    delta = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, 1], [0, 0, -1]] #상 하 좌 우 위 아래

    # print(arr)
    start_point = []
    for h in range(H) :
        for r in range(N) :
            for c in range(M) :
                if arr[h][r][c] == 1 :
                    start_point.append([r,c,h])

    ans = bfs(start_point)

    print(ans)