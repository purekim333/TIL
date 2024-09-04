import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1) :
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    min_sum = 0
    max_sum = 0

    for i in range(M):
        min_sum += arr[i]
        max_sum += arr[i]

    for count in range(N-M+1):
        M_sum = 0
        for j in range(M):
            M_sum += arr[count + j]

        if max_sum < M_sum :
            max_sum = M_sum

        if min_sum > M_sum :
            min_sum = M_sum

    result = max_sum - min_sum

    print(f'#{tc} {result}')