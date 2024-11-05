import sys; sys.stdin=open('sample_input.txt')

T = int(input())

for tc in range(1,2):
    M, A = map(int, input().split())

    A_arr = [0] + list(map(int, input().split()))
    B_arr = [0] + list(map(int, input().split()))
    Ar, Ac = 1, 1
    Br, Bc = 10, 10
    AP = [list(map(int, input().split())) for _ in range(A)]

    DIRECTION = [(0,0), [-1,0], [0,1], [1,0], [0,-1]] # 이동하지 않음, 상, 우, 하, 좌
    
    mx_sum = 0
    for time in range(M+1) :
        dAr, dAc = DIRECTION[A_arr[time]]
        dBr, dBc = DIRECTION[B_arr[time]]

        Ar += dAr
        Ac += dAc
        Br += dBr
        Bc += dBc

        for bc in range(A):
            BCc = AP[bc][0]
            BCr = AP[bc][1]
            BCrange = AP[bc][2]
            BCpower = AP[bc][3]

            if abs(Ar-BCr) + abs(Ac-BCc) <= BCrange:
                print(time, Ar, Ac)

            if abs(Br-BCr) + abs(Bc-BCc) <= BCrange:
                