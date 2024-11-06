import sys; sys.stdin=open('sample_input.txt')

T = int(input())

for tc in range(1,2):
    M, A = map(int, input().split())

    A_arr = [0] + list(map(int, input().split()))
    B_arr = [0] + list(map(int, input().split()))
    Ar, Ac = 0, 0
    Br, Bc = 9, 9
    arr = [[0] * 10 for _ in range(10)]

    for k in range(1, A+1) :
        BCc, BCr, BCrange, BCpower = map(int, input().split())

        for r in range(-BCrange, BCrange+1):
            for c in range(-(BCrange-abs(r)), BCrange-abs(r)+1):
                nr = BCr + r -1
                nc = BCc + c -1
                # print(k,'번', nr, nc)
                if 0<=nr<10 and 0<=nc<10 :
                    if arr[nr][nc] == 0 :
                        arr[nr][nc] = k
                    else:
                        if type(arr[nr][nc]) != type([]) :
                            arr[nr][nc] = [arr[nr][nc]]
                        arr[nr][nc].append(k)
        
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

        #그때 그때 최대값을 mx_sum에 다 더함
        A_sum = 0
        B_sum = 0

        if arr[Ar][Ac] != 0:
            arr[Ar][Ac]
        if arr[Br][Bc] != 0:
            pass