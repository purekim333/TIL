'''
입력으로 N X N 크기의 농장에 대한 정보가 2차 배열 형태의 값들이 주어진다. 주어진 값들은 각 셀에서 얻을 수 있는 농작물의 양이다.

지훈, 현희, 이화  3형제는 농장을 3분할 해서 농작물을 나눠 가질 계획이다.

욕심많은 지훈이 때문에 형제간 불화가 생기지 않도록 최대한 공평하게 나누어야 한다.

농장을 3분할 하는 방법은 가로선과 세로선을 그어서, 다음 그림과 같이 3개의 영역으로 나누는 것이다.

먼저 세로선을 그어서 두개의 영역으로 나누고, 왼쪽 영역에 대해 가로선을 그어서 두 개의 영역으로 나눈다.



사각영역의 가로와 세로의 크기는 최소 1이상이어야 한다.

3 분할 했을 때 세 영역에서 얻을 수 있는 농작물 총합의 최대값과 최소값의 차이가 최소가 되는 경우를 찾아보자.


[입력조건]

첫 줄에 테스트케이스 수가 주어진다.

각 테스트 케이스마다 첫 줄은 땅의 크기 N이 주어진다.

다음 N개의 줄에 각 셀을 농지로 만드는 비용이 주어진다. 비용은 0 ~ 9 사이의 값이다.

[출력조건]
'''

'''입력
3
5
2 3 2 2 1
3 1 1 1 3
3 2 3 1 3
1 1 3 2 1
2 2 2 1 1
5
3 3 2 1 1
2 1 1 3 1
3 1 3 3 2
3 1 2 2 3
2 3 1 2 2
5
1 3 2 1 3
3 1 3 2 1
3 3 1 1 2
1 3 2 2 1
1 2 3 3 2
'''

import sys; sys.stdin = open('sample_input.txt')

def make_sum(i, j, N) :
    sum_a = 0
    sum_b = 0
    sum_c = 0
    # print('인덱스', i, j, arr[i][j])
    #a 계산
    for r in range(0, i) :
        for c in range(0, j) :
            sum_a += arr[r][c]
            # print('a', r, c, arr[r][c])

    #b 계산
    for r in range(i, N) :
        for c in range(0, j) :
            sum_b += arr[r][c]
    
    #c 계산
    for r in range(N) :
        for c in range(j, N) :
            sum_c += arr[r][c]

    mx = max(sum_a, sum_b, sum_c)
    mn = min(sum_a, sum_b, sum_c)

    return mx - mn

T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    all = []
    for i in range(1, N) :
        for j in range(1, N) :
            all.append(make_sum(i, j, N))

    # print(all)
    ans = min(all)

    print(f'#{tc} {ans}')