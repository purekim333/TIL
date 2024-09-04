import sys; sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    mx_fly = 0
    for r in range(N) :
        for c in range(N) :
            fly = 0

            for m_x in range(M) :
                for m_y in range(M) :
                    if 0<= r+m_x < N and 0<= c+m_y < N :
                        fly += arr[r + m_x][c + m_y]
            
            if mx_fly < fly :
                mx_fly = fly

    print(f'#{tc} {mx_fly}')
