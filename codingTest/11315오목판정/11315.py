import sys; sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    omok = []
    for _ in range(N) :
        tmp = list(input())
        omok.append(tmp)

    ans = 'NO'
    for i in range(N) :
        for j in range(N):
            if omok[i][j] == 'o' :
                #행 검사
                if j+4 < N :
                    for m in range(5) :
                        if omok[i][j+m] != 'o' :
                            break
                    else:
                        ans = 'YES'
                #열 검사
                if i+4 < N :
                    for m in range(5) :
                        if omok[i+m][j] != 'o' :
                            break
                    else:
                        ans = 'YES'
                #오른쪽 대각선 검사
                if i+4 < N and j+4 < N :
                    for m in range(5) :
                        if omok[i+m][j+m] != 'o' :
                            break
                    else:
                        ans = 'YES'
                #왼쪽 대각선 검사
                if i+4 < N and 4 <= j:
                    for m in range(5) :
                        if omok[i+m][j-m] != 'o' :
                            break
                    else:
                        ans = 'YES'

    print(f'#{tc} {ans}')