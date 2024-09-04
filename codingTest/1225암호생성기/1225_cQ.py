'''
다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.

- 8개의 숫자를 입력 받는다.

- 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다. 

다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.

이와 같은 작업을 한 사이클이라 한다.

- 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다. 이 때의 8자리의 숫자 값이 암호가 된다.
 


[1 사이클]

 
 
[암호 도출]
 
[제약 사항]

주어지는 각 수는 integer 범위를 넘지 않는다.

마지막 암호 배열은 모두 한 자리 수로 구성되어 있다.

 
[입력]

총 10개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고, 그 다음 줄에는 8개의 데이터가 주어진다.
 
[출력]

#부호와 함께 테스트케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
'''

'''입력
1
9550 9556 9550 9553 9558 9551 9551 9551
2
2419 2418 2423 2415 2422 2419 2420 2415
'''

import sys; sys.stdin = open('input.txt')

def enQueue(data) :
    global rear
    if (rear + 1) % len(Q) == front :
        print('full')
    else :
        rear = (rear + 1) % len(Q)
        Q[rear] = data

def deQueue() :
    global front
    if front == rear :
        print('Empty')
    else:
        front = (front + 1) % len(Q)
        return Q[front]

for _ in range(10) :
    tc = int(input())

    arr = list(map(int, input().split()))

    Q = [0] * 9
    front = rear = 0

    for i in range(8) : 
        enQueue(arr[i])
        # print(Q, front, rear)

    i = 1
    while Q[rear]:
        tmp = deQueue()
        
        t = tmp - i
        if t <= 0 :
            t = 0
        enQueue(t)
        i = (i % 5) + 1

        # else:
        #     enQueue(tmp)
        #     break

    ans = []
    while front != rear :
        ans.append(deQueue())
    
    print(f'#{tc}', *ans)
    

