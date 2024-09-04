import sys; sys.stdin = open('carrot_sample_in.txt')

T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    arr = list(map(int, input().split()))

    mx_carrot = 1
    cnt = 1
    for i in range(1, N) :
        if arr[i-1] < arr[i] :
            cnt += 1
            if mx_carrot < cnt :
                mx_carrot = cnt
        
        else :
            cnt = 1

    print(f'#{tc} {mx_carrot}')


