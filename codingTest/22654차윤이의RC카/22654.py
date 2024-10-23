import sys; sys.stdin = open('sample_input.txt')

'''
6살 차윤이는 생일선물로 RC카를 선물받았다.
아직 조종이 익숙하지 않은 차윤이는 공원에서 조종 연습을 하려고 한다.

아래는 차윤이가 조종을 연습할 N x N 필드의 정보이다.
 

GGGGG
GXGTG
GGTTG
GGGYG
GTGGG

'G' : RC카가 이동 가능한 땅
'T' : RC카가 이동이 불가능한 나무

'X' : 현재 RC카의 위치
'Y' : RC카를 이동 시키고자 하는 위치

RC카의 조종기로는 아래의 동작들을 할 수 있다.
'A' : 앞으로 이동 - 나무가 있는 곳이나 필드를 벗어나는 경우에는 아무 일도 일어나지 않는다.

      (RC카가 망가지는것을 방지하고자 장애물 판단 시스템이 탑재되었다.)
'L' : 현재 바라보고 있는 방향에서 왼쪽으로 90도 회전
'R' : 현재 바라보고 있는 방향에서 오른쪽으로 90도 회전

차윤이는 RC카를 항상 위를 바라보는 방향으로 부터 조종을 시작한다.
차윤이가 RC카를 조종한 커맨드가 주어졌을 때,  목적지에 도달 할 수 있는지 구하라. 
(커맨드가 종료되었을 때, 목적지에 위치 해 있어야 한다.)

입력 

첫번째 줄에는 테스트 케이스의 개수 T가 주어진다. (1 <= T <= 10) 
각 테스트 케이스의 첫번째 줄에 필드의 크기 N이 주어진다. (2 <= N <= 5)
두번째 줄부터 N개의 줄에 걸쳐 필드의 정보가 공백 없이 주어진다.
필드의 정보는 본문의 설명을 참고하라. 
다음 줄에는 조종을 한 횟수 Q가 주어진다. (1 <= Q <= 5)
다음 Q개의 줄에는 커맨드의 길이 C와 커맨드가 공백으로 구분되어 주어진다. (1 <= C <= 50)

출력 

T개의 줄에 걸쳐 각 테스트 케이스에 대한 정답을 출력한다.
각 줄은 "#t"로 시작하고 (t는 1부터 시작하는 테스트 케이스의 번호를 의미한다.) 공백을 하나 둔 후, 정답을 출력한다. 
각 테스트케이스의 커맨드마다 목적지에 도달 할 수 있다면 1, 아니면 0을 공백으로 구분하여 출력한다.
목적지에 이동 가능 여부가 아닌, 커맨드를 전부 실행 후 목적지에 도달했는지를 확인해야 함에 유의하라.
'''

T = int(input())

class Rc():
    def __init__(self, r, c):
        self.looking = 0
        self.position = r, c
    
    def rotate(self, rotation):
        self.looking += direction_dict[rotation]
        self.looking = self.looking % 4
    
    def move(self):
        #위
        r, c = self.position
        if self.looking == 0 :
            if 0<= r-1 and arr[r-1][c] != 'T':
                r -= 1
        
        #오른쪽
        elif self.looking == 1:
            if c+1 < N and arr[r][c+1] != 'T':
                c += 1

        #아래
        elif self.looking == 2:
            if r+1 < N and arr[r+1][c] != 'T':
                r += 1

        #왼쪽
        else :
            if 0<= c-1 and arr[r][c-1] != 'T':
                c -= 1
        
        self.position = r, c

direction_dict = {
    'up' : 0,
    'right' : 1,
    'down' : 2,
    'left' : 3,
}


def move_rc(command):
    rc = Rc(start_r, start_c)
    for order in command :
        if order == 'A':
            rc.move()

        elif order == 'L':
            rc.rotate('left')

        elif order == 'R':
            rc.rotate('right')

        # print(order, rc.position, rc.looking)

    return rc.position


for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N) ]
    Q = int(input())

    q_list = []
    for _ in range(Q) :
        C, command = input().split(' ')
        q_list.append(command)

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X' :
                start_r, start_c = i, j

    ans=[]
    for cmd in q_list :
        arrive_x, arrive_y = move_rc(cmd)
        if arr[arrive_x][arrive_y] == 'Y' :
            ans.append(1)
        else :
            ans.append(0)

    print(f'#{tc}', *ans)