import sys; sys.stdin = open('algo1_sample_in.txt')

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    arr = list(input())

    max_cnt = 0
    for i in range(N) :
        s = e = i
        cnt = 1
        while arr[s] == arr[e] :
            if max_cnt < cnt :
                max_cnt = cnt
            s -= 1
            e += 1
            # print(i, s, e, arr[i], cnt)
            if 0 > s or e > N-1 :
                break
            cnt += 2


    print(f'#{tc} {max_cnt}')

