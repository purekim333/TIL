import sys; sys.stdin = open('input.txt')

'''
KGTTY
GGTTG
GWTTG
GWTWG
XGTGG

P : 잔여 포탄
K : 보급소
Y : 공격 목표
X : 현재 나의 탱크
W : 물(절대 못지나감)
G : 풀 지나갈 수 있음
T : 나무(포탄 사용해서 파괴 가능)
'''
from collections import deque

def bfs(s_r, s_c, P): #현재 위치(s_r, s_c)
    visited = [[0]*N for _ in range(N)]
    count = P
    q = deque()
    cmd = ''
    q.append((s_r, s_c, cmd, count))
    visited[s_r][s_c] = 1

    while q:
        v_r, v_c, cmd, count = q.popleft()
        print(v_r, v_c, cmd, '나무 잔여 :' ,count)
        for row in visited:
            print(*row) 

        if arr[v_r][v_c] == 'Y' :
            return cmd
        
        for dr, dc, command in [[-1,0,'U'], [0,1,'R'], [1,0,'D'], [0,-1,'L']]: #위 오 아래 왼
            nr = v_r + dr
            nc = v_c + dc
            n_cmd = cmd + command
            if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0 and arr[nr][nc] != 'W': #물이거나 방문했거나 범위를 벗어나면 못 지나감
                '''
                풀이라면 그냥 지나감(Q에 append)
                나무이고 포탄이 남아있다면 count 하나 감소 후 부시고 넘어감
                나무이고 포탄이 없다면 append 하지 않음
                보급소이면 포탄 하나 얻고 넘어감
                '''
                if arr[nr][nc] == 'T' and count>=1 :
                    count -= 1
                    q.append((nr, nc, n_cmd, count))

                elif arr[nr][nc] == 'T' and count == 0 :
                    continue
                
                elif arr[nr][nc] == 'K' :
                    count += 1
                    q.append((nr, nc, n_cmd, count))

                else : #그냥 풀밭
                    q.append((nr, nc, n_cmd, count))

                visited[nr][nc] = 1

T = int(input())

for tc in range(1, T+1):
    N, P = map(int, input().split())

    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                s_r, s_c = i, j

    command = bfs(s_r,s_c, P)

    

    print('answer :', command)

    