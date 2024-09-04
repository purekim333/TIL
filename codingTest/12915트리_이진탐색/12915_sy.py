import sys; sys.stdin = open('sample_input.txt')


T = int(input())


for tc in range(1, T+1) :
    N = int(input())
    tree = [0] * (N+1)
    cont = 1

    def bts(v) :
        global N,tree,cont
        if v > N :
            return
        
        bts(v*2)
        # print(v, end = ' ')
        tree[v] =cont
        cont+=1

        bts(v*2 + 1)


    bts(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}', end=' ')
    
    print()
