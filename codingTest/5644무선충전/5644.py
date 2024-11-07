import sys; sys.stdin=open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    M, A = map(int, input().split())

    A_arr = [0] + list(map(int, input().split()))
    B_arr = [0] + list(map(int, input().split()))
    Ar, Ac = 0, 0
    Br, Bc = 9, 9
    arr = [[0] * 10 for _ in range(10)]

    battery = [[0]*4]
    for k in range(A) :
        BCc, BCr, BCrange, BCpower = map(int, input().split())
        battery.append([BCc, BCr, BCrange, BCpower])
        for r in range(-BCrange, BCrange+1):
            for c in range(-(BCrange-abs(r)), BCrange-abs(r)+1):
                nr = BCr + r -1
                nc = BCc + c -1
                if 0<=nr<10 and 0<=nc<10 :
                    if arr[nr][nc] == 0:
                        arr[nr][nc] = k+1
                    else:
                        if type(arr[nr][nc]) != type([]):
                            arr[nr][nc] = [arr[nr][nc]]
                        arr[nr][nc].append(k+1)
    # print() 
    # for line in arr :
    #     print(*line)

    # print(battery)
    DIRECTION = [(0,0), [-1,0], [0,1], [1,0], [0,-1]] # 이동하지 않음, 상, 우, 하, 좌
    
    mx_sum = 0
    for time in range(M+1) :
        cur_sum = 0
        dAr, dAc = DIRECTION[A_arr[time]]
        dBr, dBc = DIRECTION[B_arr[time]]

        Ar += dAr
        Ac += dAc
        Br += dBr
        Bc += dBc

        A_bc = arr[Ar][Ac]
        B_bc = arr[Br][Bc]


        if type(A_bc) == type([]) :
            if type(B_bc) == type([]) :
                cur_mx = 0
                for a_bc in A_bc:
                    for b_bc in B_bc:
                        if a_bc == b_bc:
                            A_sum = battery[a_bc][3] /2
                            B_sum = battery[b_bc][3] /2
                            cur_sum = A_sum + B_sum
                            if cur_mx < cur_sum :
                                cur_mx = cur_sum
                        else :
                            A_sum = battery[a_bc][3]
                            B_sum = battery[b_bc][3]
                            cur_sum = A_sum + B_sum
                            if cur_mx < cur_sum :
                                cur_mx = cur_sum
            else:
                cur_mx = 0
                for a_bc in A_bc:
                    if a_bc == B_bc:
                            A_sum = battery[a_bc][3] /2
                            B_sum = battery[B_bc][3] /2
                            cur_sum = A_sum + B_sum
                            if cur_mx < cur_sum :
                                cur_mx = cur_sum
                    else :
                        A_sum = battery[a_bc][3]
                        B_sum = battery[B_bc][3]
                        cur_sum = A_sum + B_sum
                        if cur_mx < cur_sum :
                            cur_mx = cur_sum
                        
        
        elif type(B_bc) == type([]):
            cur_mx = 0
            for b_bc in B_bc:
                if A_bc == b_bc:
                    A_sum = battery[A_bc][3]
                    B_sum = battery[b_bc][3]
                    cur_sum = A_sum + B_sum
                    if cur_mx < cur_sum :
                         cur_mx = cur_sum
                else :
                    A_sum = battery[A_bc][3]
                    B_sum = battery[b_bc][3]
                    cur_sum = A_sum + B_sum
                    if cur_mx < cur_sum :
                        cur_mx = cur_sum

        else :
            if A_bc == B_bc:
                A_sum = battery[A_bc][3]
                B_sum = battery[B_bc][3]
                cur_mx = A_sum + B_sum
            else :
                A_sum = battery[A_bc][3]
                B_sum = battery[B_bc][3]
                cur_mx = A_sum + B_sum

        mx_sum += cur_mx

    print(f'#{tc}', mx_sum)