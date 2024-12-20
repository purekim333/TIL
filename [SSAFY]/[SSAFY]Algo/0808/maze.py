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
import sys; sys.stdin = open('sample_input.txt')

# input 데이터 저장방법 결정
# 지나간 칸을 표시 or 지나간 칸을 벽으로 막으면서 원래대로 돌아가는 것을 막아야 한다.

def fstart(N) :
    for i in range(N) :
        for j in range(N) :
            if maze[i][j] == 2:
                return i, j
    return -1, -1


T = int(input())
for tc in range(1, T+1) :
    N = int(input())

    maze = [list(map(int, input().split())) for _ in range(N)]

    #출발 위치 찾기
    sti, stj = fstart(N)

    visited = [[0] * N for _ in range(N)]
    print(f'#{tc} {}')