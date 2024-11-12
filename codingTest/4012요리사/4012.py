import sys; sys.stdin = open('sample_input.txt')

T = int(input())

def dfs(n, A, B) :
    print(n, A, B)
    if n == N:
        return
    
    if len(A) > N//2:
        return
    if len(B) > N//2 :
        return
    
    mx_sum = 0
    if len(A) == len(B) == N//2 :
        for i in range(N//2):
            for j in range(i+1, N//2):
                print(A[i], A[j])

    dfs(n+1, A+[n], B)
    dfs(n+1, A, B+[n])

for tc in range(1, 2):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N) ]

    dfs(0, [], [])

