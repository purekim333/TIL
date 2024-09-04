import sys; sys.stdin = open('sample_input.txt')

'''
1부터 N까지의 자연수를 이진 탐색 트리에 저장하려고 한다.

이진 탐색 트리는 어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.

추가나 삭제가 없는 경우에는, 완전 이진 트리가 되도록 만들면 효율적인 이진 탐색 트리를 만들수 있다.

다음은 1부터 6까지의 숫자를 완전 이진 트리 형태인 이진 탐색 트리에 저장한 경우이다.




 
완전 이진 트리의 노드 번호는 루트를 1번으로 하고 아래로 내려가면서 왼쪽에서 오른쪽 순으로 증가한다.

N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과, N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 N이 주어진다. 1<=N<=1000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
'''입력
3
6
8
15
'''

def tree(N) :
    global value
    if N == 0 :
        # val[N] = value
        # value += 1
        # print(tc, val)
        return
    
    # print(N, left[N], right[N])
    tree(left[N])
    # print(N, '탐색중', value)
    val[N] = value
    value += 1
    tree(right[N])

    

T = int(input())

for tc in range(1, T+1) :
    V = int(input())
    E = V - 1

    par = [0] * (V+1)
    left = [0] * (V+1)
    right = [0] * (V+1)

    val = [0] * (V+1)
    value = 1

    for i in range(1, V//2+1) :
        
        p = i
        l = 2*i
        r = 2*i + 1

        left[p] = l
        if r <= (V):
            right[p] = r
            par[r] = p
        par[l] = p

    # print(par)
    tree(1)
    # root = 
    ans = val[V//2]
    # print(val)
    print(f'#{tc} {val[1]} {ans}')
    