'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.

주어진 미로 밖으로는 나갈 수 없다.
 

다음은 5x5 미로의 예이다.
 

13101

10101

10101

10101

10021

 

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
 

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 도착할 수 있으면 1, 아니면 0 을 출력한다.
'''
'''
입력
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
'''

import sys; sys.stdin = open('sample_input.txt')

def my_push(data) :
    global top
    top += 1
    stack[top] = data

def my_pop() :
    global top
    tmp = top
    top -= 1
    return stack[tmp]

def chk_direction(x,y) :
    available = []
    for i in range(4) :
        xi = x + dx[i]
        yi = y + dy[i]
        if 0<=xi< N and 0<= yi < N:
            if maze[xi][yi] != 1 :
                available.append((xi,yi))
    return available

def dfs(v_x, v_y) :
    ans = None
    if maze[v_x][v_y] == 3:
        ans = 1
        return ans
    visited[v_x][v_y] = 1
    # print(v, end = ' ')
    G = chk_direction(v_x, v_y)
    if not G :
        return
    for w_x, w_y in G :
        # print(v, w, G[v], visited[w])
        if visited[w_x][w_y] != 1:
            ans = dfs(w_x, w_y)
            if ans == 1 :
                return ans
            
    if ans == 1:
        return ans
    else :
        return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    maze = [list(map(int, list(input()))) for _ in range(N) ]

    visited = [[0] * N for _ in range(N)]

    stack = [0] * N**2
    top = -1

    dx = [0, 1, 0, -1] # 오 밑 왼 위
    dy = [1, 0, -1, 0] # 오 밑 왼 위

    for x in range(N) :
        for y in range(N) :
            if maze[x][y] == 2 :
                start_x = x
                start_y = y

    ans = dfs(start_x, start_y)

    print(f'#{tc} {ans}')


    