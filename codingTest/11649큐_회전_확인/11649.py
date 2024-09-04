'''
N개의 숫자로 이루어진 수열이 주어진다. 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.

 
     


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 첫 줄에 N과 M이 주어지고, 다음 줄에 10억 이하의 자연수 N개가 주어진다. 3<=N<=20, N<=M<=1000,

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.
'''

'''입력
3
3 10
5527 731 31274 
5 12
18140 14618 18641 22536 23097 
10 23
17236 31594 29094 2412 4316 5044 28515 24737 11578 7907 
'''

import sys; sys.stdin = open('sample_input.txt')

def enQueue(data) :
    global rear
    if rear == len(Q) - 1:
        Q.append(data)
        rear += 1
    else :
        rear += 1
        Q[rear] = data

def deQueue() :
    global front
    if front == rear :
        print('Empty!')
    else :
        front += 1
        return Q[front]

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    Q = arr
    front = -1
    rear = N-1

    # for k in range(N) :
    #     enQueue(arr[k])
    #     print('시작', Q, front, rear)

    for _ in range(M) :
        # for i in range(N) :
        enQueue(deQueue())
        # print(Q, front, rear)
        
    ans = Q[front + 1]

    print(f'#{tc} {ans}')       




