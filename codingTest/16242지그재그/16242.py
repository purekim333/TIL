'''
초기값이 0으로 채워진 10 x 10 2차 배열에서 사각형 모양의 좌상단 모서리와 너비, 높이가 주어지면, 지그재그로 순회하면서 방문하는 위치에 1부터 시작해서 1씩 증가하는 값을 저장해보자.

정사각형의 위치가 (3, 4) 이고 너비=3, 높이=4 면 다음과 같이 출력한다.

0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 2 3 0 0 0
0 0 0 0 6 5 4 0 0 0
0 0 0 0 7 8 9 0 0 0
0 0 0 0 12 11 10 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0



[입력]

첫 줄에 테스트케이스 개수(T)가 주어진다.
각 테스트케이스마다 사각 영역의 좌상단 모서리의 위치(행, 열)와 너비, 높이가 주어진다.


[출력]
첫 줄에 #과 함께 테스트케이스 번호를 출력한다.
다음 줄 부터 10줄에 공백으로 구분된 10개의 정수를 출력한다.
'''
'''
3
3 4 3 4
5 2 1 5
2 3 4 6
'''
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1) :
    start_x, start_y, length, height = map(int, input().split())

    arr = [[0] * 10 for _ in range(10)]

    n = start_x + height
    m = start_y + length

    i = 1
    for x in range(height) :
        for y in range(length) :
            dx = start_x + x
            dy = start_y + y

            arr[dx][dy + (m-1-dy-y) * (x%2)] = i
            i += 1
            # print(x, y, m, m-1-y+start_y)
    print(f'#{tc}')
    for ary in arr :
        print(*ary)