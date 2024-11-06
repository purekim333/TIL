import sys; sys.stdin=open('sample_input.txt')

T = int(input())

for tc in range(1,2):
    M, A = map(int, input().split())

    A_arr = [0] + list(map(int, input().split()))
    B_arr = [0] + list(map(int, input().split()))
    Ar, Ac = 1, 1
    Br, Bc = 10, 10
    arr = [[0] * 10 for _ in range(10)]
    for line in arr :
        print(line)
    for k in range(A) :
        BCc, BCr, BCrange, BCpower = map(int, input().split())

        for r in range(-BCrange, BCrange+1):
            for c in range(-(BCrange-abs(r)), BCrange-abs(r)+1):
                nr = BCr + r -1
                nc = BCc + c -1
                # print(k,'번', nr, nc)
                if 0<=nr<10 and 0<=nc<10 :
                    BC = str(k)+'번'
                    arr[nr][nc]=(BC)
        
    print() 
    for line in arr :
        print(*line)


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
            pass

            if abs(Ar-BCr) + abs(Ac-BCc) <= BCrange:
                # print(time, Ar, Ac)
                pass

            if abs(Br-BCr) + abs(Bc-BCc) <= BCrange:
                pass