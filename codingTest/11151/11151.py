'''
N 개의 정수값들이 주어질 때, 인접한 두 원소의 합이 최대인 경우를 찾으시오.

인접한 두 원소는 입력으로 주어지는 순서가 연속적인 2개의 값을 의미한다.

[입력]

첫줄에 테스트케이스 개수가 주어진다.

각 테스트 케이스마다 첫 줄에 N이 주어진다. (5 < N <= 100)

다음 줄에 공백을 두고 N개의 정수 값이 주어진다. (-200 <= 정수값 <= 200)


[출력]

#과 테스트케이스 번호를 출력하고, 인접한 두 수의 합이 최대인 값을 출력한다.
'''

'''
3
5
9 -1 -8 4 -1
5
4 -10 -4 9 7
10
-20 2 -19 -4 -18 19 -19 -20 -12 11
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    arr = list(map(int, input().split()))

    
    mx_num = 0

    for i in range(N-1) :
        con_num = 0
        for count in range(2) :
            con_num += arr[i + count]

        if mx_num < con_num :
            mx_num = con_num

    print(f'#{tc} {mx_num}')
    