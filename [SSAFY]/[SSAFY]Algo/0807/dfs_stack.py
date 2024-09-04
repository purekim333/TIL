'''
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
import sys; sys.stdin = open('dfs_input.txt')

def my_push(data) :
    global top
    top += 1
    stack[top] = data

def my_pop() :
    global top
    tmp = top
    top -= 1
    return stack[tmp]

V, E = map(int, input().split())
arr = list(map(int, input().split()))

G = [[] for _ in range(V+1)]

stack = [0] * V
top = -1

visited = [0] * (V+1)

for i in range(0, E * 2, 2) :
    u, v = arr[i], arr[i+1]
    G[v].append(u)
    G[u].append(v)

def dfs(v):
    visited[v] = 1
    print(v, end= ' ')
    while True :
        for w in G[v] :
            if visited[w] != 1 :
                my_push(v)
                print(top, v)
                v = w
                visited[v] = 1
                print(v, end= ' ')
                break
        else :
            if top != -1 :
                v = my_pop()
            else :
                break

dfs(1)
                



















# s시작정점, V 정점개수(1번부터인 정점의 마지막정점)
# 방문한 정점을 표시
# # 스택생성
# 시작정점 방문표시
# v에 인접하고, 방문안한 w가 있으면
# push(v) 현재 정점을 push하고
# w에 방문
# w에 방문 표시
# for w, v부터 다시 탐색
# 남은 인접정점이 없어서 break가 걸리지 않은경우
# 이전 갈림길을 스택에서 꺼내서... if TOP > -1
# 되돌아갈 곳이 없으면 남은 갈림길이 없으면 탐색종료
# while True:



# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     adjL = [[] for _ in range(V+1)]
#     arr = list(map(int, input().split()))
#     for i in range(E):
#         v1, v2 = arr[i*2], arr[i*2+1]
#         adjL[v1].append(v2)
#         adjL[v2].append(v1)

#     DFS(1, V)