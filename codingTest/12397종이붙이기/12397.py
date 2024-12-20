'''
어린이 알고리즘 교실의 선생님은 경우의 수 놀이를 위해, 그림처럼 가로x세로 길이가 10x20, 20x20인 직사각형 종이를 잔뜩 준비했다.

   


그리고 교실 바닥에 20xN 크기의 직사각형을 테이프로 표시하고, 이 안에 준비한 종이를 빈틈없이 붙이는 방법을 찾아보려고 한다. N이 30인 경우 다음 그림처럼 종이를 붙일 수 있다.





10의 배수인 N이 주어졌을 때, 종이를 붙이는 모든 경우를 찾으려면 테이프로 만든 표시한 영역을 몇 개나 만들어야 되는지 계산하는 프로그램을 만드시오. 직사각형 종이가 모자라는 경우는 없다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 N이 주어진다. 10≤N≤300, N은 10의 배수

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
'''
입력
3
30
50
70
'''

import sys; sys.stdin = open('sample_input.txt')

def comb(n,r):
    memo = [[0] * 50 for _ in range(50)]

    for i in range(n+1) :
        for j in range(i+1) :
            if j == 0 or i == j :
                memo[i][j] = 1
            else :
                memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

    return memo[n][r]

# def get_ans(N, R) :
#     if N - R <= 1:
#         return comb(N,R) * (2**R)
#     else :
#         return get_ans(N-1, R+1)


T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    N = N//10

    '''
    3 -> 111 , 12, 21, 
            -> 1 + 2*2
    4 -> 1111, 112, 121, 211, 22 
            -> 1 + 3*2 + 1*4
    5 -> 11111, 1112, 1121, 1211, 2111, 122, 212, 221
            -> 1 + 4*2 + 3*4
    6 -> 111111, 11112, 11121, 11211, 12111, 21111, 1122, 1221, 2211, 1212, 2121, 2112, 222  
            -> 1 + 5*2 + 6*4 + 1*8
    7 -> 1111111, 111112, 111121, 111211, 112111, 12111, 21111, 11122, 11221, 12211, 22111, 11212, 12121, 21211, 12112, 21121, 21112, 1222, 2122, 2212, 2221
            -> 1 + 6*2 + 10*4 + 4*8

    1 3 5 11 21 43         
    '''
    i = 0
    ans = 0
    while N-i >= 0 :
        ans += comb(N, i) * (2**i)
        N -= 1
        i += 1
         
    print(f'#{tc} {ans}')

    
    # import sys; sys.stdin = open('4869.txt', 'r')

    # memo = [0] * 101
    # memo[1], memo[2] = 1, 3
    # for i in range(3, 101):
    #     memo[i] = memo[i - 1] + memo[i - 2]*2

    # for tc in range(1, int(input()) + 1):
    #     N = int(input())
    #     print(memo[N//10])








