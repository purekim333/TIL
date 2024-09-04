'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, V) : #시작점 s, 정점수 V
    # 준비
    visited = [0] * (V+1)   # visited 생성
    D = [0] * (V+1) #출발점에서 w까지 최단거리
    P = [0] * (V+1) # 이전에 정점 -> 최단경로 트리
    Q = []    # Q 생성
    Q.append(s)    # 시작점 인큐
    visited[s] = 1    # 시작점 방문 표시
    # 탐색
    while Q: #Q가 비어있지 않으면 / 탐색할 정점이 남아있으면/ 만든 Q 종류에 따라 설정
        t = Q.pop(0)    # t <- deQueue
        print(t)    # 처리
        for w in G[t] :    # t에 인접이고, 인큐된적이 없으면
            if visited[w] == 0:
                Q.append(w)     # 인큐하고 인큐됨 표시
                visited[w] =  1 # 방문표시
                D[w] = D[t] + 1 # 출발점에서 w 까지 거리
                P[w] = t        # 이전의 정점

V, E = map(int, input().split())
arr = list(map(int, input().split()))

G = [[] for _ in range(V+1)]  #인접리스트
                                # G = [[],
                                #          [],
                                #          [],
                                #          ]
                                # G[1][] -> 1번 정점의 인접 정점 

for i in range(E) :
    v1, v2 = arr[i*2], arr[i*2+1]
    G[v1].append(v2)
    G[v2].append(v1)  # 방향 없는 무향 그래프

bfs(2, V) # 출발점, 정점수