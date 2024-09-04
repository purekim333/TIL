# import sys;sys.stdin = open('algo2_sample_in.txt')

def perm(k, ch, per_lst) :
    if k == N:
        tmp = list(map(int, ch))
        per_lst.append(tmp)
        return


    for i in range(len(eilien)) :
        if visited[i] == 0 :
            tmp = str(eilien[i])
            ch += tmp
            # print(k, i, ch, visited)
            visited[i] = 1
            perm(k+1, ch, per_lst)
            ch = ch[:k]
            visited[i] = 0

T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    Aij = [list(map(int, input().split())) for _ in range(N)]

    eilien = list(map(str, range(N)))
    visited = [0] * N
    per_lst = []
    ch = ''

    perm(0, ch, per_lst)

    min_fatal = float('inf')
    for case in per_lst :
        fatal = 0
        for order in range(N-1) :
            first = case[order]
            next = case[order + 1]
            fatal += Aij[first][next]
        if min_fatal > fatal :
            min_fatal = fatal

    print(f'#{tc} {min_fatal}')
