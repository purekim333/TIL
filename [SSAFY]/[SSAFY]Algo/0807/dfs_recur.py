import sys; sys.stdin = open('dfs_input.txt')

V, E = map(int, input().split())

arr = list(map(int, input().split()))

G = [[] for _ in range(V+1)]

visited = [0] * (V + 1)

for i in range(0, E*2, 2) :
    u, v = arr[i], arr[i+1]
    G[u].append(v)
    G[v].append(u)

def dfs(v) :
    visited[v] = 1
    print(v, end = ' ')
    for w in G[v] :
        # print(v, w, G[v], visited[w])
        if visited[w] != 1:
            dfs(w)

# print(G)
dfs(1)
    