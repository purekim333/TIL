import sys; sys.stdin = open('sample_input.txt')

'''
6살 차윤이는 앞으로 이동, 왼쪽으로 90도 회전, 오른쪽으로 90도 회전이 가능한 RC카를 작년 생일에 선물받았다.
아빠와의 오랜 연습을 통해, 차윤이는 이제RC카를 아주 능숙하게 다룰 수 있게 되었다
 
차윤이는 출발지에서 목적지까지 최소의 조작으로 이동시킬 수 있다.
(최단 거리가 아닌, 최소 리모컨 조작 횟수임에 유의하라.)

어느 날, 나무에 가로 막혀 RC카를 목적지까지 이동시킬 수 없어 차윤이는 눈물을 뚝뚝 흘리고 있다.
아빠는 울고 있는 차윤이를 위해 나무를 베기로 결심하였다. 
모든 아버지는 위대하다고 하지만, 모든 나무를 벨 수는 없다.

 N x N 크기의 필드 정보와 아빠가 벨 수 있는 최대 나무의 수가 주어졌을 때, 차윤이가 RC카를 목적지까지 이동시키기 위한 최소 조작 횟수를 구하라.
차윤이는 항상 위를 바라보는 상태로 RC카의 조작을 시작한다.

[예시]
아래와 같이 5 x 5 크기의 필드 정보가 주어진다.

그리고 아빠는 최대 2개의 나무를 벨 수 있다

5 2     //5 x 5 크기의 필드, 아빠는 나무를 최대 2회 벨수 있다.
GGTGG
GXTTG
GGTTG
GGTYG
GGTGG

필드의 정보는 아래와 같다. 
'G' : RC카가 이동 가능한 땅
'T' : RC카가 이동이 불가능한 나무
'X' : 현재 RC카의 위치
'Y' : RC카를 이동 시키고자 하는 위치

(0, 2) 위치의 나무를 베면 11번의 조작으로 목적지에 도달할 수 있다.
전진 -> 우회전 -> 전진 -> 전진 (나무 베기 1회)-> 전진 -> 우회전 -> 전진 -> 전진 -> 전진 -> 우회전 -> 전진
아래 맵에서 베어진 나무는 '.' 로 표기하고 있다 
​​​​​​​G   G > . > G > G
    ^           v
G   X   T   T   G
                v
G   G   T   T   G
                v
G   G   T   Y < G

G   G   T   G   G

(3, 2) 위치의 나무를 베면 7번의 조작으로 목적지에 도달할 수 있다. 그리고 이것이 최소 조작 횟수이다.
우회전 -> 우회전 -> 전진 -> 전진 -> 좌회전 -> 전진(나무 베기 1회) -> 전진
아래 맵에서 베어진 나무는 '.' 로 표기하고 있다 
​​​​​​​
G   G   T   G   G
                
G   X   T   T   G
    v            
G   G   T   T   G
    v            
G   G > . > Y   G

G   G   T   G   G

입력

첫번째 줄에는 테스트 케이스의 개수 T가 주어진다. (1 <= T <= 10) 
각 테스트 케이스의 첫번째 줄에 필드의 크기 N과 나무를 벨 수 있는 횟수 K가 주어진다. (2 <= N <= 10, 0 <= K <= 5)
두번째 줄부터 N개의 줄에 걸쳐 필드의 정보가 공백 없이 주어진다.
필드의 정보는 본문의 설명을 참고하라. 
'''
def dfs(v_r, v_c,k, direction, distance):
    global tree
    global final_distance
    global path
    global tmp_path

    visited[v_r][v_c] = 1
    position = v_r*N + v_c
    tmp_path.append(position)
    # print(k, position, tmp_path,distance, final_distance)
    
    if arr[v_r][v_c] == 'Y' :
        # print('도착!')
        if final_distance > distance :
            final_distance = distance
            path = tmp_path
        tree = 0
        # print('현재까지의 경로', path, final_distance)
        return

    if arr[v_r][v_c] == 'T' :
        tree += 1
        # print('나무발견! 현재까지 벤 나무', tree)
        if tree > K :
            # print('벨 수 있는 최대 나무 초과!')
            return

    if distance > final_distance :
        # print('경로가 너무 길어용')
        return

    for dr, dc in [[-1,0], [0,1], [1,0], [0,-1]] : #위 오 아래 왼
        n_r = v_r + dr
        n_c = v_c + dc
        if 0<= n_r < N and 0<= n_c < N and visited[n_r][n_c] == 0 :
            tmp_tree = tree
            tmp_direction = direction
            next_position = n_r*N + n_c

            move = 0
            relation = next_position - position
            # print(tmp_path, distance, final_distance)
            # print(position, next_position,relation, direction)
            if relation == direction :
                move += 1
            elif relation == -direction:
                direction = relation
                move += 3
            else :
                direction = relation
                move += 2

            # print(position, next_position, move)

            dfs(n_r, n_c, k+1, direction, distance+move)

            direction = tmp_direction
            tree = tmp_tree
            tmp_path = tmp_path[:k+1]
            visited[n_r][n_c] = 0

    if len(path) == 0:
        return -1
    
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = [list(input()) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X' :
                s_r, s_c = i, j

    v_r = s_r
    v_c = s_c
    position = v_r*N + v_c
    final_distance = 9999
    path = []
    tmp_path = []
    tree = 0

    dfs(v_r, v_c, 0, -N, 0)

    if len(path) == 0:
        final_distance = -1

    print(f'#{tc}', final_distance)


        
