'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개체 수를 의미한다.

아래는 N=5 의 예이다.

파리 킬러 스프레이를 한 번만 뿌려 최대한 많은 파리를 잡으려고 한다. 스프레이의 노즐이 + 형태로 되어있어, 스프레이는 + 혹은 x 형태로 분사된다. 스프레이를 M의 세기로 분사하면 노즐의 중심이 향한 칸부터 각 방향으로 M칸의 파리를 잡을 수 있다.
다음은 M=3 세기로 스프레이르 분사한 경우 파리가 퇴치되는 칸의 예로, +또는 x 중 하나로 분사된다. 뿌려진 일부가 영역을 벗어나도 상관없다.



한 번에 잡을 수 있는 최대 파리수를 출력하라.

 

[제약 사항]

1. N 은 5 이상 15 이하이다.
2. M은 2 이상 N 이하이다.
3. 각 영역의 파리 갯수는 30 이하 이다.

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
다음 N 줄에 걸쳐 N x N 배열이 주어진다.
'''
import sys 
sys.stdin = open('in1.txt')

#입력
T = int(input())
for tc in range(1, T+1) :

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 제로 패딩
    '''
    인덱스 에러를 없애기 위해 파리채 구간 양 옆에 M-1 너비의 0인 배열들을 추가해 준다.
    '''
    zero_arr = []
    for row in arr :
        zero_arr.append([0] * (M-1) + row + [0] * (M-1)) #행을 하나하나 순회하면서 왼쪽 오른쪽에 0인 배열 추가
    up_down = [[0] * (N + 2*(M-1))] * (M-1) # 열에도 추가
    zero_arr = up_down + zero_arr + up_down

    plus_d_x = [1, 0 , -1, 0] # 오 위 왼 밑
    plus_d_y = [0, 1, 0, -1] # 오 위 왼 밑

    multi_d_x = [1, -1, -1, 1] # 대각선 오 왼 왼 오
    multi_d_y = [1, 1, -1, -1] # 대각선 오 왼 왼 오

    mx_death_p = 0
    mx_death_x = 0
    
    for row_index in range(M-1, len(zero_arr)-(M-1)) :
        for col_index in range(M-1, len(zero_arr)-(M-1)):
            sum_death_p = 0
            sum_death_x = 0
            for m in range(1, M):
                for i in range(4) :
                    sum_death_p += zero_arr[row_index + (m * plus_d_x[i])][col_index + (m * plus_d_y[i])]
                    sum_death_x += zero_arr[row_index + (m * multi_d_x[i])][col_index + (m * multi_d_y[i])]
            sum_death_p += zero_arr[row_index][col_index]
            sum_death_x += zero_arr[row_index][col_index]

            if mx_death_p < sum_death_p :
                mx_death_p = sum_death_p

            if mx_death_x < sum_death_x :
                mx_death_x = sum_death_x

    print(f"#{tc} {max(mx_death_p, mx_death_x)}")
