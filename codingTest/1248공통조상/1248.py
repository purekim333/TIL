import sys; sys.stdin = open('input.txt')

'''
이진 트리에서 임의의 두 정점의 가장 가까운 공통 조상을 찾고, 그 정점을 루트로 하는 서브 트리의 크기를 알아내는 프로그램을 작성하라.
 





예를 들어, 위의 이진 트리에서 정점 8과 13의 공통 조상은 정점 3과 1 두 개가 있다.

이 중 8, 13에 가장 가까운 것은 정점 3이고, 정점 3을 루트로 하는 서브 트리의 크기(서브 트리에 포함된 정점의 수)는 8이다.

[입력]

가장 첫 번째 줄에 테스트케이스의 수가 주어진다.

각 케이스의 첫 번째 줄에는 정점의 개수 V(10 ≤ V ≤ 10000)와 간선의 개수 E, 공통 조상을 찾는 두 개의 정점 번호가 주어진다.

각 케이스의 두 번째 줄에는 E개 간선이 나열된다. 간선은 항상 “부모 자식” 순서로 표기된다.

위에서 예로 든 트리에서 정점 5와 8을 잇는 간선은 “5 8”로 표기된다.

정점의 번호는 1부터 V까지의 정수이며, 루트 정점은 항상 1번이다.
'''

T = int(input())

def dfs(cur, prv, depth):
    global size
    root[cur] = prv
    for next in tree[cur] :

        dfs(next, cur, depth+1)
        size_arr[cur] += size_arr[next]



for tc in range(1, T+1) :
    V, E, N1, N2 = map(int, input().split())

    root = [[] for _ in range(V+1)]
    size_arr = [1] * (V+1)

    tree = [[] for _ in range(V+1)]
    arr = list(map(int, input().split()))

    for i in range(0, 2*E, 2) :
        tree[arr[i]].append(arr[i+1])
    
    
    size = 1
    dfs(1, 1, 0)

    anc_a_lst = set()
    anc_b_lst = set()
    anc_a = N1
    anc_b = N2
    while True :
        if anc_a == anc_b: break
        anc_a = root[anc_a]
        anc_b = root[anc_b]

        anc_a_lst.add(anc_a)
        anc_b_lst.add(anc_b)

    both = anc_a_lst & anc_b_lst

    ans = max(both)
    print(f'#{tc}', ans, size_arr[ans])
    