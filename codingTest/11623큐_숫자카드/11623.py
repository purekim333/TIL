'''
N 장의 카드에 1번 부터 N번 까지 숫자가 부여되어 있으며, 1번 카드가 제일 위에, 2번 카드가 그 다음, 
N번 카드가 가장 아래인 상태로 쌓여있다.

숫자 카드가 한 장 남을 때까지 다음 동작을 반복하게 된다.

- 가장 위에 있는 카드를 가져와서 버린다.
- 그 다음, 가장 위에 있는 카드를 가장 아래에 있는 카드 밑으로 옮긴다.

N = 4인 경우를 생각해 보자.

카드는 위에서부터 [1, 2, 3, 4] 의 순서로 놓여있다. 1을 버리면 [2, 3, 4]가 남는다.
여기서 2를 아래로 옮기면 [3, 4, 2]가 된다. 3을 버리면 [4, 2]가 되고, 4를 밑으로 옮기면 [2, 4]가 된다.
마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.

N이 주어졌을 때, 가장 마지막에 남는 카드를 구하시오.


[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  (1 <= T <= 20)
각 테스트 케이스 마다 한줄에 N 이 주어진다. (1 <= N <= 100000)


[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 마지막에 남는 카드 번호를 출력한다.
'''
'''입력
3
4
5
7
'''

import sys; sys.stdin = open('sample_input.txt')

def enQueue(data) :
    global rear
    if rear == N -1 :
        print('FULL')
    else :
        rear += 1
        Q[rear] = data

def deQueue() :
    global front
    if rear == front :
        print('Empty')
        
    else :
        front += 1
        return Q[front]

T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    arr = list(range(1, N+1))

    Q = [0] * N
    front = rear = -1

    for j in range(N) :
        enQueue(arr[j])

    i = 0
    while rear - front >= 1:
        # print(tc, Q, rear, front)
        if i%2 == 0 :
            deQueue()
        else :
            tmp = deQueue()
            Q.append(tmp)
            rear += 1

        i += 1

    ans = Q[front]
    
    print(f'#{tc} {ans}')





