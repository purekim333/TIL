'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
 

10 1 9 2 8 3 7 4 6 5
 

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.
'''
'''
입력
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11 
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26 
'''
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    ai = list(map(int, input().split()))
    
    for i in range(N) :
        mx_i = i
        mn_i = i
        for j in range(i+1, N) :
            if ai[mn_i] > ai[j] :
                mn_i = j
            if ai[mx_i] < ai[j] :
                mx_i = j
        if i % 2 == 1 : #홀수 (작은수 배열)        
            ai[i], ai[mn_i] = ai[mn_i], ai[i]
        elif i % 2 == 0 : # 짝수 (큰수 배열)
            ai[i] ,ai[mx_i] = ai[mx_i] , ai[i]
    str_lst = list(map(str, ai[:10]))
    answer = ' '.join(str_lst)
    print(f'#{tc} {answer}')
        
