'''
N개의 양의 정수가 첫번째부터 N번째까지 주어진다. 최대값의 위치와 최소값의 위치의 차이를 절대값으로 출력 하시오.

단, 가장 작은 수가 여러 개이면 먼저 나오는 위치로 하고 가장 큰 수가 여러 개이면 마지막으로 나오는 위치로 한다.

예를 들어, {1, 1, 2, 3, 3} 가 주어지면 최대값의 위치는 5이고, 최소값의 위치는 1이다. 따라서 두 값 차이의 절대값은 4이다.

[입력]

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 10 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 100 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 10 )

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

'''
입력
3
5
1 1 2 3 3
10
3 10 5 5 8 3 9 1 3 3 
20
4 1 6 7 9 4 1 4 8 4 1 6 5 3 1 4 3 1 10 10 
'''

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    
    ai = list(map(int, input().split()))
    
    min_i = 0
    max_i = 0

    for i in range(N) :
        if ai[min_i] > ai[i] :
            min_i = i
        if ai[max_i] <= ai[i] :
            max_i = i
            
    if max_i < min_i :
        min_i, max_i = max_i, min_i
    answer = max_i - min_i
    
    print(f'#{tc} {answer}')
            
        