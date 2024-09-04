'''
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.
 

3 4 + .
 

Forth에서는 동작은 다음과 같다.
 

숫자는 스택에 넣는다.

연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.

‘.’은 스택에서 숫자를 꺼내 출력한다.

 

Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
 

다음은 Forth 연산의 예이다.
 

코드

출력

4 2 / .

2

4 3 - .

1

 

 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다. 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.

나눗셈의 경우 항상 나누어 떨어진다.

 

[출력]
 

#과 1번부터인 테스트케이스 번호, 빈칸에 이어 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.
'''
'''입력
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .
'''

import sys; sys.stdin = open('sample_input.txt')

def my_push(data):
    global top
    top += 1
    stack[top] = data

def my_pop() :
    global top
    tmp = top
    top -= 1
    return stack[tmp]

def change_type(a, string, b) :
    if string == '*' :
        return a * b
    if string == '/' :
        return a // b
    if string == '+' :
        return a + b
    if string == '-' :
        return a - b

first = {'*' , '/'}
second = {'+', '-'}

T = int(input())

for tc in range(1, T+1) :
    arr = list(input().split())

    stack = [0] * len(arr)
    top = -1

    for elmnt in arr :
        print(elmnt, stack, top)
        if elmnt.isdecimal() : # 숫자일경우
            my_push(int(elmnt))

        elif elmnt in first|second : #연산자일 경우
            if top <= 0 : #남아있는 숫자가 없는경우
                ans = 'error'
                break
            elif stack[top] in first|second: # 남아있는 것이 연산자인 경우
                ans = 'error'
                break
            # if type(stack[top]) == type(2) and type(stack[top-1]) == type(2): #연산가능할 경우
            else :    # 숫자가 2개 이상 남아있고 연산가능
                b = my_pop()
                a = my_pop()
                result = change_type(a, elmnt, b)
                my_push(result)
            # elif elmnt in first : #연산 불가능하고 elmnt가 상위 연산자
            #     my_push(elmnt)
            # elif elmnt in second and stack[top] in second :
            #     my_push(elmnt)
            # else :
            #     ans = 'error'
            #     break

        else : # . 을 만날 경우
            if top == 0 :
                ans = stack[top]
                break
            else :
                ans = 'error'
                break
    
    print(f'#{tc} {ans}')






