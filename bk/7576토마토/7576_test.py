from collections import deque

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