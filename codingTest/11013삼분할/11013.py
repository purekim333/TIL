'''
입력으로 N개의 양수들이 주어진다. 3개의 연속적인 구간으로 나누고, 각 구간에 속한 값들의 총합을 구한다.

세 구간의 합 중에서 최대값과 최소값의 차이가 최소가 되는 경우를 찾아서 차이를 출력한다.

(2, 6, 8, 5, -8) 과 같이 5개의 정수가 주어지면 (2)(6)(8 5 -8) 으로 3분할 하면 합이 2, 6, 5 가 되고 최대/최소의 차이는 4(= 6 - 2)가 된다.


[입력조건]

첫 줄에 테스트케이스 수가 주어진다.

다음으로 정수의 개수 N이 주어진다. (5 <= N <= 50)

다음 줄에 공백으로 구분된 N개의 정수 값이 주어진다. ( -10 <= 정수값 <= 10)

[출력조건]

#〉 과 케이스 번호를 출력하고 3분할 시 최소와 최대의 차이가 최소인 값을 출력한다.
'''
'''입력
3
5
2 6 8 5 -8 
5
-2 -2 -5 -8 5 
6
1 -5 7 -6 8 3 
'''

import sys; sys.stdin=open('sample_input.txt')

T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    arr = list(map(int, input().split()))

    min_cnt = []
    for i in range(1, N-1):
        for j in range(i+1, N) :
            a = arr[:i]
            b = arr[i:j]
            c = arr[j:]

            min_cnt.append(max(sum(a), sum(b), sum(c)) - min(sum(a),sum(b),sum(c)))

    ans = min(min_cnt)

    print(f'#{tc} {ans}')
