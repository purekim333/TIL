'''
NxN인 2차원 배열 A에서, 어떤 원소의 상하좌우에 있는 원소를 이웃 원소라고 한다.

어떤 원소와 이웃 원소들의 합이 최대인 경우를 찾으시오.

원소의 위치에 따라 이웃 원소는 4개가 아닐 수도 있다.

[입력]

- 첫줄에 테스트 케이스 개수가 입력된다.

- 테스트 케이스의 첫줄에는 2차원 배열의 크기 N 이 주어진다. (5 <= N <= 30)

- 다음 N 개의 줄에 공백으로 구분된 N 개의 정수가 주어진다. (0이상 30이하의 값)

[출력]

- '#테스트케이스 번호' 를 출력하고, 최대합을 공백으로 구분해서 출력한다.
'''

'''
입력
3
5
28 25 12 12 27
18 3 1 24 16
14 24 18 18 9
23 7 13 4 8
21 29 7 8 22
5
2 8 19 27 18
7 12 20 1 12
17 23 23 22 24
4 6 28 8 11
15 29 15 3 12
5
18 16 17 13 8
23 20 4 29 6
25 3 18 14 8
5 17 23 21 25
23 19 17 16 23
'''

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    arr = [[0] * (N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+2)]

    max_sum = 0

    for i in range(1, N+1) :
        sum_element = 0
        for j in range(1, N+1) :
            sum_element = arr[i][j] + arr[i-1][j] + arr[i+1][j] + arr[i][j-1] + arr[i][j+1]
            if max_sum < sum_element:
                max_sum = sum_element
    
    print(f'#{tc} {max_sum}')