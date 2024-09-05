# 현재 (r, c) 위 퀸을 두는 선택
# cols[0...k-1] : 이전의 퀸에 대한 선택
def notPossible(cols, r, c) :
    pass



N = 4
visit = [0]*N #순열에서 중복
cols = [0]*N #순서를 기록

# cols[0] <- 0번행에서 열의 위치
def nQueen(k) :
    if k == N :
        print(cols)
    else :
        for i in range(N) :
            if visit[i] : continue
            # k번 행에 열의 위치 i로 선택
            if notPossible(cols, k, i) : continue
            visit[i] = 1
            cols[k] = i
            nQueen(k+1)
            visit[i] = 0

nQueen(0)