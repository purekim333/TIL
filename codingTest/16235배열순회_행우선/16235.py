T = int(input())

for tc in range(1, T+1):
    a, b, N = map(int, input().split())

    arr = [[0] * 10 for _ in range(10)]

    c =1
    for i in range(N):
        for j in range(N) :
            arr[a+i][b+j] = c
            c += 1

    print(f'#{tc}')
    for ary in arr :
        print(*ary)