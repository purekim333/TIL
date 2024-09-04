'''
오목은 바둑판에 검은 바둑알과 흰 바둑알을 교대로 놓아서 겨루는 게임이다. 바둑판에는 19개의 가로줄과 19개의 세로줄이 그려져 있는데 가로줄은 위에서부터 아래로 1번, 2번, ... ,19번의 번호가 붙고 세로줄은 왼쪽에서부터 오른쪽으로 1번, 2번, ... 19번의 번호가 붙는다.



위의 그림에서와 같이 같은 색의 바둑알이 연속적으로 다섯 알을 놓이면 그 색이 이기게 된다. 여기서 연속적이란 가로, 세로 또는 대각선 방향 모두를 뜻한다. 즉, 위의 그림은 검은색이 이긴 경우이다. 하지만 여섯 알 이상이 연속적으로 놓인 경우에는 이긴 것이 아니다.

입력으로 바둑판의 어떤 상태가 주어졌을 때, 검은색이 이겼는지, 흰색이 이겼는지 또는 아직 승부가 결정되지 않았는지를 판단하는 프로그램을 작성하시오. 단, 검은색과 흰색이 동시에 이기거나 검은색 또는 흰색이 두 군데 이상에서 동시에 이기는 경우는 입력으로 들어오지 않는다.

입력
19줄에 각 줄마다 19개의 숫자로 표현되는데, 검은 바둑알은 1, 흰 바둑알은 2, 알이 놓이지 않는 자리는 0으로 표시되며, 숫자는 한 칸씩 띄어서 표시된다.

출력
첫줄에 검은색이 이겼을 경우에는 1을, 흰색이 이겼을 경우에는 2를, 아직 승부가 결정되지 않았을 경우에는 0을 출력한다. 검은색 또는 흰색이 이겼을 경우에는 둘째 줄에 연속된 다섯 개의 바둑알 중에서 가장 왼쪽에 있는 바둑알(연속된 다섯 개의 바둑알이 세로로 놓인 경우, 그 중 가장 위에 있는 것)의 가로줄 번호와, 세로줄 번호를 순서대로 출력한다.
'''
import sys; sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(19)]

N = 19

wb_lst = [0, 1, 2] # 바닥, 흑, 백
B = 1
W = 2

def chk_omok(r, c) :
    wb = arr[r][c]

    #4방향 탐색
    dr = [0, 1, 1, 1] #우 우밑대 밑 좌밑대
    dc = [1, 1, 0, -1]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        cnt = 1
        dol_lst = [[r,c]]
        while 0<=nr<N and 0<=nc<N and arr[nr][nc] == wb :
            dol_lst.append([nr,nc])
            cnt += 1
            nr += dr[i]
            nc += dc[i]

        if cnt == 5 : #오목이고
            # print(r,c, wb)
            chk_x = r-dr[i] #이전돌이 범위 안에 있고 다른색 돌이라면
            chk_y = c-dc[i]
            # print(r, c, chk_x, chk_y, arr[chk_x][chk_y])
            if chk_x < 0 or chk_y < 0 or chk_x > N or chk_y > N :
                return wb, dol_lst
            # print(chk_x, chk_y, arr[chk_x][chk_y], wb)
            if 0<= chk_x < N and 0<= chk_y < N and arr[chk_x][chk_y] != wb :
                return wb, dol_lst
            
    return 0, None

winner_lst = []
for r in range(N) :
    for c in range(N):
        if arr[r][c] != 0 :
            wb, dol_lst = chk_omok(r,c)
            if wb != 0 :
                winner_lst.append((wb, dol_lst))
                # print(winner_lst)

if not winner_lst :
    print(0)
else :
    wb, dol_lst  = winner_lst[0]
    min_r = 20
    min_c = 20
    for r, c in dol_lst :
        if min_c > c:
            # print(min_x)
            min_r = r
            min_c = c
    print(wb)
    print(min_r+1, min_c+1)


    


