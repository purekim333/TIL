import sys
sys.stdin = open('sample_input.txt')

T = int(input())
A = [1,2,3,4,5,6,7,8,9,10,11,12]
for tc in range(1, T+1) :
    N, K = map(int, input().split())

    subset_lst = []
    for i in range(2 ** 12) :
        subset = []
        for j in range(12) :
            if i & (1 << j) :
                subset.append(A[j])
        subset_lst.append(subset)

    cnt = 0
    for s in subset_lst :
        if len(s) == N and sum(s) == K :
            cnt += 1

    print(f'#{tc} {cnt}')