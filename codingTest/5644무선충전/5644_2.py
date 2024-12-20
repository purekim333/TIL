import sys; sys.stdin=open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    M, A = map(int, input().split())

    A_arr = [0] + list(map(int, input().split()))
    B_arr = [0] + list(map(int, input().split()))
    Ar, Ac = 0, 0
    Br, Bc = 9, 9

    BC = [list(map(int, input().split())) for _ in range(A)]

    DIRECTION = [(0,0), [-1,0], [0,1], [1,0], [0,-1]] # 이동하지 않음, 상, 우, 하, 좌
    
    # print(BC)
    mx_sum = 0
    for time in range(M+1) :
        dAr, dAc = DIRECTION[A_arr[time]]
        dBr, dBc = DIRECTION[B_arr[time]]

        Ar += dAr
        Ac += dAc
        Br += dBr
        Bc += dBc

        A_cnt = []
        B_cnt = []
        for battery in range(A):
            
            cur_sum = 0
            BCc, BCr, BCrange, BCpower = BC[battery]
            BCc -= 1
            BCr -= 1

            if abs(Ar-BCr) + abs(Ac-BCc) <= BCrange:
                A_cnt.append(battery)
            if abs(Br-BCr) + abs(Bc-BCc) <= BCrange:
                B_cnt.append(battery)


        ab_mx = 0
        if A_cnt or B_cnt :
            if A_cnt and B_cnt:
                for a in A_cnt:
                    a_bc = BC[a][3]
                    for b in B_cnt:
                        b_bc = BC[b][3]
                        if a==b:
                            a_bc = int(a_bc/2)
                            b_bc = int(b_bc/2)
                            ab_sum = a_bc + b_bc
                            if ab_mx < ab_sum :
                                ab_mx = ab_sum
                        else:
                            a_bc = BC[a][3]
                            b_bc = BC[b][3]
                            ab_sum = a_bc + b_bc
                            if ab_mx < ab_sum :
                                ab_mx = ab_sum


            
            elif A_cnt :
                for a in A_cnt:
                    a_bc = BC[a][3]
                    ab_sum = a_bc
                    if ab_mx < ab_sum :
                        ab_mx = ab_sum



            elif B_cnt:
                for b in B_cnt:
                    b_bc = BC[b][3]
                    ab_sum = b_bc
                    if ab_mx < ab_sum :
                        ab_mx = ab_sum


        mx_sum += ab_mx
        # print(time, ab_mx)

    print(f'#{tc}', mx_sum)