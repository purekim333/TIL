import sys; sys.stdin = open('sample_input.txt')

'''
완전 이진 트리의 리프 노드에 1000이하의 자연수가 저장되어 있고, 리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어있다고 한다.

다음은 리프 노드에 저장된 1, 2, 3이 주어졌을 때, 나머지 노드에 자식 노드의 합을 저장한 예이다.
  

	
리프 노드 저장 값	자식 노드의 합을 저장한 상태

N개의 노드를 갖는 완전 이진 트리의 노드 번호는 루트가 1번이 되며, 같은 단계에서는 왼쪽에서 오른쪽으로 증가, 단계가 꽉 차면 다음단계의 왼쪽부터 시작된다.

완전 이진 트리의 특성상 1번부터 N번까지 빠지는 노드 번호는 없다.

리프 노드의 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장한 다음, 지정한 노드 번호에 저장된 값을 출력하는 프로그램을 작성 하시오.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L이 주어지고, 다음 줄부터 M개의 줄에 걸쳐 리프 노드 번호와 1000이하의 자연수가 주어진다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
T = int(input())

def bst(v) :
    global num
    if v == 0 :
        return
    
    bst(left[v])
    bst(right[v])
    num += node[v]
    print(num)


for tc in range(1, T+1) :
    N, M, L = map(int, input().split())

    par = [0] * (N+1)
    right = [0] * (N+1)
    left = [0] * (N+1)
    node = [0] * (N+1)

    for i in range(1, N//2+1) :
        left[i] = 2*i
        right[i] = 2*i + 1
        par[2*i] = i
        if (2*i + 1) <= N :
            par[2*i + 1] = i

    print(left)
    print(right)
    print(par)
    for _ in range(M) :
        m, val = map(int, input().split())
        node[m] = val

    num = 0

    bst(1)
    print(node)
    print(num)
