import sys; sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    for _ in range(M) :
        i, j = map(int, input().split())

        for cnt in range(i-1, i-1+j) :
            if cnt < N :
                # print(arr)
                # print(cnt, arr[cnt])
                arr[cnt] = arr[i-1]

    print(f'#{tc}', *arr)
