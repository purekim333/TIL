'''
입력으로 두 정수 N, K 가 주어진다. 그리고, 다음 줄에 1이상 1000이하의 N개 정수들이 공백으로 구분되어 주어진다. 

K 번째로 작은 수를 찾아서 출력하시오. 

단, 동일한 값이 여러 개 존재하는 경우는 순서상 하나로 간주한다. 

 

첫 번째 예제 입력과 같이, N = 7, K = 5 인 경우를 보자.

7 개의 숫자 ( 1, 3, 5, 6, 4, 4, 6 ) 이 주어 질 때,  1번째로 작은 수는 1이고, 2번째는 2 이고, 3번째는 4이고, 4번째는 5가 되고, 5번째로 작은 수는 6이 된다.

 

[입력]

첫 줄에는 테스트 케이스 수가 주어진다.

다음 줄에 N, K가 주어진다. N 은 1000 보다 크지 않고, K 는 답으로 가능한 수가 주어진다.

다음 줄에 N 개의 정수들이 공백으로 구분되어 주어진다. (1 <= 정수 <= 1000) 

 

[출력]
"#" 과 테스트 케이스 번호를 출력, 공백을 두고 K 번째 작은 수를 출력한다.
'''

'''
입력
3
7 5
1 3 5 6 4 4 6
10 5
1 3 4 2 3 7 1 6 9 2
10 5
4 7 5 5 1 5 4 4 3 3
'''

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1) :
    N, K = map(int, input().split())

    arr = list(map(int, input().split()))

    #최대값 찾기
    max_n = 0
    for num in arr :
        if max_n < num :
            max_n = num
    
    tmp = [0] * N

    count = [0] * (max_n + 1)

    for i in range(N) :
        count[arr[i]] += 1

    for i in range(1, max_n + 1):
        count[i] += count[i-1]

    for i in range(N-1, -1, -1) :
        count[arr[i]] -= 1
        tmp[count[arr[i]]] = arr[i]

    step = 1
    for i in range(1, N) :
        if tmp[i] > tmp[i-1] :
            step += 1
        
        if step == K :
            answer = tmp[i]

    print(f'#{tc} {answer}')


    