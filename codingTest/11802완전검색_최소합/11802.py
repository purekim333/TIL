import sys; sys.stdin = open('sample_input.txt')

'''
그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.

맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.
 

1

2

3

2

3

4

3

4

5


그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.

[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13
 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

'''입력
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1
'''

from collections import deque

T = int(input())

# def bfs(N) :
#     visited = [[10*N*N] * N for _ in range(N)]
#     delta = [[0,1],[1,0]]
#     q = deque()
#     q.append((0,0))
#     visited[0][0] = arr[0][0]

#     while q :
#         v_r, v_c = q.popleft()
#         if v_r == N-1 and v_c == N-1 :
#             return visited[v_r][v_c]
        
#         for d_r, d_c in delta:
#             n_r = v_r + d_r
#             n_c = v_c + d_c
#             if 0<= n_r < N and 0<=n_c < N :
#                 q.append((n_r, n_c))
#                 if visited[n_r][n_c] > arr[n_r][n_c] + visited[v_r][v_c]:
#                     visited[n_r][n_c] = arr[n_r][n_c] + visited[v_r][v_c]

def dfs(v_r, v_c, cnt) :
    global path
    delta = [[0,1],[1,0]]
    visited[0][0] = arr[0][0]
    
    if visited[v_r][v_c] > path :
        return
    
    if v_r == N-1 and v_c == N-1 :
        if path > visited[v_r][v_c] :
            path = visited[v_r][v_c]
        return
    
    for d_r, d_c in delta :
        n_r = v_r + d_r
        n_c = v_c + d_c
        if 0 <= n_r < N and 0 <= n_c < N :
            visited[n_r][n_c] = visited[v_r][v_c] + arr[n_r][n_c]
            dfs(n_r, n_c, cnt)

    

for tc in range(1, T+1) :
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    path = 10000000000
    ans = dfs(0,0, arr[0][0])

    print(f'#{tc} {path}')



