import sys; sys.stdin = open('sample_input.txt')

'''
해야 할 V개의 작업이 있다. 이들 중에 어떤 작업은 특정 작업이 끝나야 시작할 수 있으며, 이를 선행 관계라 하자.

이런 작업의 선행 관계를 나타낸 그래프가 주어진다.

이 그래프에서 각 작업은 하나씩의 정점으로 표시되고 선행 관계는 방향성을 가진 간선으로 표현된다.

단, 이 그래프에서 사이클은 존재하지 않는다 (사이클은 한 정점에서 시작해서 같은 정점으로 돌아오는 경로를 말한다).

아래 그림은 이런 그래프의 한 예다.
'''

from collections import deque
def bfs() :
    q = deque()

    for i in range(1, V+1) :
        if I[i] == 0:
            q.append(i)

    while q:
        v = q.popleft()
        print(v, end=' ')

        for n in G[v]:
            I[n] -= 1
            if I[n] > 0 : continue
            q.append(n)


for tc in range(1, 11):
    V, E = map(int, input().split())

    arr = list(map(int, input().split()))

    G = [[] for _ in range(V+1)]
    I = [0]*(V+1)

    for i in range(0, 2*E, 2):
        G[arr[i]].append(arr[i+1])
        I[arr[i+1]] += 1

    print(f'#{tc}', end=' ')

    bfs()
    print()