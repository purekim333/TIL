import sys; sys.stdin = open('sample_input.txt')

'''
2016년은 삼성전자가 러시아 현지법인을 설립한지 20주년이 된 해이다. 이를 기념해서 당신은 러시아 국기를 만들기로 했다.

먼저 창고에서 오래된 깃발을 꺼내왔다. 이 깃발은 N행 M열로 나뉘어 있고, 각 칸은 흰색, 파란색, 빨간색 중 하나로 칠해져 있다.

당신은 몇 개의 칸에 있는 색을 다시 칠해서 이 깃발을 러시아 국기처럼 만들려고 한다. 다음의 조건을 만족해야 한다.

위에서 몇 줄(한 줄 이상)은 모두 흰색으로 칠해져 있어야 한다.
다음 몇 줄(한 줄 이상)은 모두 파란색으로 칠해져 있어야 한다.
나머지 줄(한 줄 이상)은 모두 빨간색으로 칠해져 있어야 한다.

이렇게 러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 개수의 최솟값을 구하여라.


          

첫 번째 예제이다. 왼쪽에 있는 그림이 입력이다. 중간에 있는 그림에 X가 적힌 칸들을 새롭게 색칠하여 오른쪽에 있는 그림과 같은 깃발을 만들면 최적이다.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 두 정수 N,M(3≤N,M≤50)이 공백으로 구분되어 주어진다.

다음 N개의 줄에는 M개의 문자로 이루어진 문자열이 주어진다. i번 째 줄의 j번째 문자는 깃발에서 i번째 행 j번째 열인 칸의 색을 의미한다.

‘W’는 흰색, ‘B’는 파란색, ‘R’은 빨간색을 의미한다. ‘W’, ‘B’, ‘R’외의 다른 문자는 입력되지 않는다.


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 개수의 최솟값을 구하여 T 줄에 걸쳐서 출력한다
'''
'''입력
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW
'''

T = int(input())

for tc in range(1, T+1 ):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]

    new_arr = [[0] *M for _ in range(N)]

    #2분할 하여
    #각 행에 흰 파 빨 을 만들면서
    #칠해지는 칸을 세보자

    mn_cnt = float('inf')
    for w_row in range(N-2) :
        for b_row in range(w_row+1, N-1):
            r_row = b_row + 1
            cnt = 0
            # print(w_row, b_row, r_row)
            for r in range(0, w_row+1) :
                for c in range(M) :
                    if arr[r][c] != 'W' :
                        # print(r, c, arr[r][c], cnt+1)
                        # new_arr[r][c] = 'W'
                        cnt += 1

            for r in range(w_row+1, b_row+1) :
                for c in range(M) :
                    if arr[r][c] != 'B' :
                        # print(r, c, arr[r][c], cnt+1)
                        # arr[r][c] = 'B'
                        cnt += 1

            for r in range(b_row+1, N) :
                for c in range(M) :
                    if arr[r][c] != 'R' :
                        # print(r, c, arr[r][c], cnt+1)
                        # arr[r][c] = 'R'
                        cnt += 1

            if mn_cnt > cnt :
                mn_cnt = cnt

    print(f'#{tc} {mn_cnt}')
            
                

