import sys;sys.stdin = open('algo1_sample_in.txt')

T = int(input())

for tc in range(1, T+1) :
    N, K = map(int, input().split())

    arr = list(map(int, input().split()))

    if arr[0] == 1 :
        energy = K
    else :
        energy = 0

    i = 0
    while True :
        if arr[i] == 1:
            energy = K

        if i == N-1 or energy == 0 :
            break

        energy -= 1
        i += 1
    print(f'#{tc} {i+1}')




