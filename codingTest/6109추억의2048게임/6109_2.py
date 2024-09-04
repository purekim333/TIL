import sys;sys.stdin=open('s_input.txt')

def make_ary(arr, N, move) :
    tmp_arr = [] #left, up, right, down
    if move == 0 : #왼쪽으로 정렬
        for row in arr :
            tmp_lst = []
            for item in row :
                if item != 0 :
                    tmp_lst.append(item)
            tmp_lst += [0] * (N-len(tmp_lst))
            tmp_arr.append(tmp_lst)

        return tmp_arr

    elif move == 1 : #위쪽으로 정렬
        new_tmp_arr = [[0] * N for _ in range(N)]
        for j in range(N) :
            tmp_lst = []
            for i in range(N) :
                if arr[i][j] != 0 :
                    tmp_lst.append(arr[i][j])
            tmp_lst += [0] * (N-len(tmp_lst))
            # print(tmp_lst)
            tmp_arr.append(tmp_lst)

        # print(tmp_arr)

        for r in range(N):
            for c in range(N) :
                new_tmp_arr[r][c] = tmp_arr[c][r]

        return new_tmp_arr

    elif move == 2 : #오른쪽으로 정렬
        for row in arr :
            tmp_lst = []
            for item in row :
                if item != 0 :
                    tmp_lst.append(item)
            tmp_lst = [0] * (N-len(tmp_lst)) + tmp_lst
            tmp_arr.append(tmp_lst)

        return tmp_arr

    elif move == 3 : #아래쪽으로 정렬
        new_tmp_arr = [[0] * N for _ in range(N)]
        for j in range(N) :
            tmp_lst = []
            for i in range(N) :
                if arr[i][j] != 0 :
                    tmp_lst.append(arr[i][j])
            tmp_lst = [0] * (N-len(tmp_lst)) + tmp_lst
            tmp_arr.append(tmp_lst)

        # print(tmp_arr)

        for r in range(N):
            for c in range(N) :
                new_tmp_arr[r][c] = tmp_arr[c][r]

        return new_tmp_arr

T = int(input())

for tc in range(1, T+1) :
    N, S = input().split()
    N = int(N)

    arr = [list(map(int, input().split())) for _ in range(N)]

    new_arr = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1] #좌 하 우 상
    dj = [1, 0, -1, 0] #left, up, right, down

    if S == 'left' : # 행 거꾸로 탐색
        move = 0
        arr = make_ary(arr, N, move)
        # print(arr)
        for num in range(N) :
        
            initail_state = [[num, 0],
                            [0, num],
                            [num, N-1],
                            [N-1, num]] #left, up, right, down
            
            arr_ni, arr_nj = initail_state[move]
            new_ni, new_nj = initail_state[move]

            while arr_nj < len(arr) :
                if arr_nj == len(arr) -1 :
                    new_arr[new_ni][new_nj] = arr[arr_ni][arr_nj]

                else :
                    if arr[arr_ni][arr_nj] == arr[arr_ni + di[move]][arr_nj + dj[move]] :
                        new_arr[new_ni][new_nj] = arr[arr_ni][arr_nj] + arr[arr_ni + di[move]][arr_nj + dj[move]]
                        arr_ni += di[move]
                        arr_nj += dj[move]
                        
                    else :
                        new_arr[new_ni][new_nj] = arr[arr_ni][arr_nj]

                if arr[arr_ni][arr_nj] == 0 :
                    arr_ni += di[move]
                    arr_nj += dj[move]

                else :
                    arr_ni += di[move]
                    arr_nj += dj[move]

                    new_ni += di[move]
                    new_nj += dj[move]

    elif S == 'up' : # 행 거꾸로 탐색
        move = 1
        arr = make_ary(arr, N, move)
        for num in range(N) :
        
            initail_state = [[num, 0],
                            [0, num],
                            [num, N-1],
                            [N-1, num]] #left, down, right, up
            
            arr_ni, arr_nj = initail_state[move]
            new_ni, new_nj = initail_state[move]

            while arr_ni < len(arr) :
                if arr_ni == len(arr) -1 :
                    new_arr[new_ni][new_nj] = arr[arr_ni][arr_nj]

                else :
                    if arr[arr_ni][arr_nj] == arr[arr_ni + di[move]][arr_nj + dj[move]] :
                        new_arr[new_ni][new_nj] = arr[arr_ni][arr_nj] + arr[arr_ni + di[move]][arr_nj + dj[move]]
                        arr_ni += di[move]
                        arr_nj += dj[move]
                    
                    else :
                        new_arr[new_ni][new_nj] = arr[arr_ni][arr_nj]

                if arr[arr_ni][arr_nj] == 0 :
                    arr_ni += di[move]
                    arr_nj += dj[move]

                else :
                    arr_ni += di[move]
                    arr_nj += dj[move]

                    new_ni += di[move]
                    new_nj += dj[move]

    
    if S == 'right' : # 행 거꾸로 탐색
        move = 2
        arr = make_ary(arr, N, move)
        for num in range(N) :
        
            initail_state = [[num, 0],
                            [0, num],
                            [num, N-1],
                            [N-1, num]] #left, up, right, down
            
            arr_ni, arr_nj = initail_state[move]
            new_ni, new_nj = initail_state[move]

            while 0 <= arr_nj :
                if arr_nj == 0 :
                    new_arr[new_ni][new_nj] = arr[arr_ni][arr_nj]

                else :
                    if arr[arr_ni][arr_nj] == arr[arr_ni + di[move]][arr_nj + dj[move]] :
                        new_arr[new_ni][new_nj] = arr[arr_ni][arr_nj] + arr[arr_ni + di[move]][arr_nj + dj[move]]
                        arr_ni += di[move]
                        arr_nj += dj[move]
                        
                    else :
                        new_arr[new_ni][new_nj] = arr[arr_ni][arr_nj]

                if arr[arr_ni][arr_nj] == 0 :
                    arr_ni += di[move]
                    arr_nj += dj[move]

                else :
                    arr_ni += di[move]
                    arr_nj += dj[move]

                    new_ni += di[move]
                    new_nj += dj[move]
    
    
    if S == 'down' : # 행 거꾸로 탐색
        move = 3
        arr = make_ary(arr, N, move)
        for num in range(N) :
        
            initail_state = [[num, 0],
                            [0, num],
                            [num, N-1],
                            [N-1, num]] #left, up, right, down
            
            arr_ni, arr_nj = initail_state[move]
            new_ni, new_nj = initail_state[move]

            while 0 <= arr_ni :
                if arr_ni == 0 :
                    new_arr[new_ni][new_nj] = arr[arr_ni][arr_nj]

                else :
                    if arr[arr_ni][arr_nj] == arr[arr_ni + di[move]][arr_nj + dj[move]] :
                        new_arr[new_ni][new_nj] = arr[arr_ni][arr_nj] + arr[arr_ni + di[move]][arr_nj + dj[move]]
                        arr_ni += di[move]
                        arr_nj += dj[move]
                        
                    else :
                        new_arr[new_ni][new_nj] = arr[arr_ni][arr_nj]

                if arr[arr_ni][arr_nj] == 0 :
                    arr_ni += di[move]
                    arr_nj += dj[move]

                else :
                    arr_ni += di[move]
                    arr_nj += dj[move]

                    new_ni += di[move]
                    new_nj += dj[move]
    
    
    print(f'#{tc}')
    for row in new_arr:
        print(*row)
    
    '''
    4 8 2 4 0
    4 4 2 0 8
    8 0 2 4 4
    2 2 2 2 8
    0 2 2 0 0
    '''