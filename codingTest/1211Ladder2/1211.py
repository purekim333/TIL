'''
점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.

김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.

사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 최단거리로 바닥에 도착하게 되는지 궁금해졌다. 이를 구해보자.

아래 <그림 1>의 예를 살펴보면, 출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 추가되고(이 예에서는 2개가 추가됨) 이 막대들 사이에 가로 방향의 선들이 또한 랜덤하게 연결된다.

X=0인 출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.

방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.

최단거리로 바닥에 도착하려면 X=4인 출발점에서 출발해야 하므로 답은 4가 된다. 해당 경로는 별도로 표시하였다.
 


<그림 1> 사다리 게임에 대한 설명(미니맵)

아래 <그림 2>와 같은 100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서, 모든 출발점을 검사하여 바닥까지 가장 짧은 이동 거리를 갖는 시작점 x(복수 개인 경우 가장 큰 x좌표)를 반환하는 코드를 작성하라.(‘0’으로 채워진 평면상에 사다리는 연속된 ‘1’로 표현된다.)
 
 
<그림 2> 테스트케이스에 의해 생성되는 실제 사다리의 모습
 
[제약사항]

한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우는 없다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도착하게 되는 출발점의 x좌표를 출력한다.
'''

import sys
sys.stdin = open('input.txt')

def chkLadder_hor(arr, x, y, down, left, right) :
    if 0 < y < 99 :
        if arr[x][y-1] == 1 :
            down = False
            left = True
            right = False
            y = y + left_y
            return x, y, down, left, right
        elif arr[x][y+1] == 1 :
            down = False
            left = False
            right = True
            y = y + right_y
            return x, y, down, left, right
        else : 
            down = True
            left = False
            right = False
            x = x + down_x
            return x, y, down, left, right
    elif y == 99 :
        if arr[x][y-1] == 1 :
            down = False
            left = True
            right = False
            y = y + left_y
            return x, y, down, left, right
        else :
            down = True
            left = False
            right = False
            x = x + down_x
            return x, y, down, left, right
    else :
        if arr[x][y+1] ==1 :
            down = False
            left = False
            right = True
            y = y + right_y
            return x, y, down, left, right
        else:
            down = True
            left = False
            right = False
            x = x + down_x
            return x, y, down, left, right
        
def chkLadder_ver(arr, x, y, down, left, right) :
    if x < 100 :
        if arr[x+1][y] == 1 :
            down = True
            left = False
            right = False
            x = x + down_x
            return x, y, down, left, right
        else : 
            down = False
            left = left
            right = right
            if left :
                y = y + left_y
            elif right :
                y = y + right_y
            return x, y, down, left, right
    


for _ in range(10) :
    tc = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    start_point = []
    for j in range(100) :
        if arr[0][j] == 1 :
            start_x = 0
            start_y = j
            start_point.append((start_x, start_y))

    
    down = True
    left = False
    right = False

    right_y = 1
    left_y = -1
    down_x = 1

    x,y = start_point[0]

    min_cnt = float('inf')
    ans = y
    for x,y in start_point :
        cnt = 0
        ans_x = y
        while x < 100 :
            if down :
                x, y, down, left, right = chkLadder_hor(arr, x, y, down, left, right)
                # print('down', x,y)
            elif left :
                x, y, down, left, right = chkLadder_ver(arr, x, y, down, left, right)
                # print('left', x,y)
            elif right :
                x, y, down, left, right = chkLadder_ver(arr, x, y, down, left, right)
                # print('right', x,y)
            else :
                print('비상상황')
            cnt += 1
        if min_cnt > cnt :
            min_cnt = cnt
            ans = ans_x

    print(f'#{tc} {ans}')