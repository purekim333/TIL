T = int(input())

for tc in range(1, T+1) :
    a, b, M, N = map(int, input().split())

    arr = [ [0] * 10 for _ in range(10)]

    k = 1
    for j in range(M):
        for i in range(N) :
            arr[a + i][b + j] = k
            k += 1

    print(f'#{tc}')
    for ary in arr :
        print(*ary)