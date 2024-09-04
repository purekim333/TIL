import sys; sys.stdin = open('input.txt')

'''
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+4+5*6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"34+56*+7+"

변환된 식을 계산하면 44를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.
'''

'''입력
101
9+5*2+1+3*3*7*6*9*1*7+1+8*6+6*1*1*5*2*4*7+4*3*8*2*6+7*8*4*5+3+7+2+6+5+1+7+6+7*3*6+2+6+6*2+4+2*2+4*9*3
79
4+4*3*4*9+2+7*4*7+7*7*9*5*2+8*8+2*6*7*3*7*9*3*4+8+8*9+3+9+6+9+4*1+6*3+5+1+7+5*1
...
'''

def my_push(data):
    global top
    top += 1
    stack[top] = data

def my_pop() :
    global top
    tmp = top
    top -= 1
    return stack[tmp]

for tc in range(1, 11) :
    N = int(input())

    arr = list(input())

    stack = [0] * N
    top = -1
    
    postfix = []

    for data in arr :
        # data가 숫자면 stack에 집어넣고
        # data가 연산자라면 pop 시켜서 연산식에 저장하고 다음 data를 기다린다.
        # 다음에 들어오는 data가 숫자라면 더해서 sum에 저장

        # print(data, '가 들어왔음')
        
        if data.isdecimal() :
            postfix.append(int(data))
            # print(data, top, stack[:3], postfix)

        else :
            if top == -1 :
                my_push(data)
                # print(data, top, stack[:3], postfix)
            else :
                if data == '*' :
                    while True :
                        if stack[top] == '*' :
                            tmp = my_pop()
                            postfix.append(tmp)
                            # print(data, top, stack[:3], postfix)
                        else : 
                            my_push(data)
                            # print(data, top, stack[:3], postfix)
                            break
                else :
                    while top > -1 :
                        tmp = my_pop()
                        postfix.append(tmp)
                        # print(data, top, stack[:3], postfix)
                    my_push(data)
                    # print(data, top, stack[:3], postfix)
    while top > -1 :
        last = my_pop()
        postfix.append(last)
    # print(postfix)
    # print(stack, top)

    for item in postfix :
        if type(item) == type(3) :
            my_push(item)
            # print(item, top, stack[:5])
        
        else :
            b = my_pop()
            a = my_pop()
            if item == '+' :
                tmp = a + b
            elif item == '*' :
                tmp = a * b
            my_push(tmp)
            # print(a, item, b, tmp, top, stack[:5])

    # # if top != -1 :
    # #     b = my_pop()
    # #     a = my_pop()
    # #     c = my_pop()
    # #     if c == '+' :
    # #         tmp = a + b
    # #     elif c == '*' :
    # #         tmp = a * b
    # #     my_push(tmp)
    # #     print(a, item, b, tmp, top)


    # print(stack)
    print(f'#{tc} {stack[top]}')