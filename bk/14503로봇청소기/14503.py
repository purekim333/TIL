import sys; sys.stdin = open('input.txt')

'''
로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 방은 
$N \times M$ 크기의 직사각형으로 나타낼 수 있으며, 
$1 \times 1$ 크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북 중 하나이다. 방의 각 칸은 좌표 
$(r, c)$로 나타낼 수 있고, 가장 북쪽 줄의 가장 서쪽 칸의 좌표가 
$(0, 0)$, 가장 남쪽 줄의 가장 동쪽 칸의 좌표가 
$(N-1, M-1)$이다. 즉, 좌표 
$(r, c)$는 북쪽에서 
$(r+1)$번째에 있는 줄의 서쪽에서 
$(c+1)$번째 칸을 가리킨다. 처음에 빈 칸은 전부 청소되지 않은 상태이다.

로봇 청소기는 다음과 같이 작동한다.

현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
현재 칸의 주변 
$4$칸 중 청소되지 않은 빈 칸이 없는 경우,
바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
현재 칸의 주변 
$4$칸 중 청소되지 않은 빈 칸이 있는 경우,
반시계 방향으로 
$90^\circ$ 회전한다.
바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
1번으로 돌아간다.
'''
direction = [[-1,0], [0,1], [1,0], [0,-1]]

def chk_clean(v_r, v_c, visited):
    for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]] : #위 왼 아래 오
        nr = v_r + dr
        nc = v_c + dc
        if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and arr[nr][nc] == 0: #청소 가능하면
            return True
    else :
        # print('불가능 !')
        # print(nr, nc)
        return False
        
def rotate_and_chk(vr, vc, vd, visited):
    nd = (vd+3)%4
    dr, dc = direction[nd]
    next_r = vr + dr
    next_c = vc + dc
    if 0<=next_r<N and 0<=next_c<M and visited[next_r][next_c] == 0 and arr[next_r][next_c] != 1 :
        return next_r, next_c, nd
    else :
        return vr, vc, nd

def clean(r, c, d):
    vr, vc, vd = r, c, d
    visited = [ [0]*M for _ in range(N)]
    while True :
        # print('현재위치 : ', vr,vc,vd)
        visited[vr][vc] = 1
        if chk_clean(vr, vc, visited):
            vr, vc, vd = rotate_and_chk(vr,vc,vd,visited)
        else :
            dr, dc = direction[vd]
            nr = vr-dr
            nc = vc-dc
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0:
                vr, vc = nr, nc
            else :
                return visited
            

N , M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = clean(r,c,d)

count = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 1:
            count += 1

print(count)
