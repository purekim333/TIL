'''
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.


[예제]

N이 3일 경우,
 



N이 4일 경우,
 


[제약사항]

달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 N이 주어진다.


[출력]

각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

'''입력
2    
3   
4     
'''

import sys
sys.stdin = open('input.txt')

# def make_delta(N, direction) :
#     if N == 2 :
#         beta = direction[0] * N + direction[1] * (N-1) + direction[2] * (N-1)
#         return beta
#     else :
#         delta = direction[0] * N + direction[1] * (N-1) + direction[2] * (N-1) + direction[3] * (N-2)
#         return delta + make_delta(N-2, direction)

def make_delta(dx, dy, N) :
    direction_x = [dx[0]] * (N-1)
    direction_y = [dy[0]] * (N-1)

    count = 0
    for k in range(1, N) :

        direction_x += [dx[(k + count)%4]] * (N-k)            #dx[1] dx[2] dx[3] dx[0] dx[1] dx[2] dx[3] dx[2] dx[3]
        direction_x += [dx[(k + count +1)%4 ]] * (N-k)      #dx[2] dx[3] dx[4]

        direction_y += [dy[(k+count)%4]] * (N-k)            
        direction_y += [dy[(k+count+1)%4]] * (N-k)

        count += 1
    return direction_x, direction_y

T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    direction_x, direction_y = make_delta(dx,dy, N)

    x_index = 0
    y_index = 0
    for i in range(1, N*N) :
        arr[x_index][y_index] = i
        x_index += direction_x[i-1]
        y_index += direction_y[i-1]
        
    arr[x_index][y_index] = N*N

    

    print(f'#{tc}')
    for lst in arr:
        print(*lst)
    