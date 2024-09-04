'''
List1 의 Gravity 문제 

가로 100이 아니라 N인 조건입니다.

90도로 리스트를 기울였을 떄 낙하거리가 가장 큰 것을 찾으시오



[입력]
- 첫줄에 테스트 케이스 개수가 주어진다.
- 다음으로 N이 주어진다.
- 다음으로 공백으로 구분된 N개의 정수가 주어진다.

[출력]
- '#'과 테스트케이스 번호와 공백을 두고 답을 출력한다.
'''

'''
3
9
7 4 2 0 0 6 0 7 0
9
7 4 2 0 0 6 7 7 0
20
52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    arr = list(map(int, input().split()))

    mx_fall = 0

    for index in range(N) :
        count = 0
        current_box = arr[index]
        for floor in range(index+1, N) :
            if arr[index] <= arr[floor] :
                count += 1

        fall = N - 1 - index - count

        if mx_fall < fall :
            mx_fall = fall

    print(f'#{tc} {mx_fall}')





