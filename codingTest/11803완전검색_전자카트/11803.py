import sys; sys.stdin = open('sample_input.txt')

'''
골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.

두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.

e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91

e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89

 

e

1

2

3

도착

1

0

18

34

 

2

48

0

55

 

3

18

7

0

 

출발

 

 

 

 


이 경우 최소 소비량은 89가 된다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 100이하의 자연수가 주어진다. 3<=N<=10

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

import copy

def perm(cnt, N) :
    if cnt == N :
        lst.append(1)
        tmp_lst = lst.copy()
        final.append(tmp_lst)
        # print('final',final)
        lst.pop()
        return
    
    # print(cnt, N)
    for i in range(2, N+1) :
        if visited[i] == 1 :
            continue
        visited[i] = 1
        lst.append(i)
        # print('before',lst)
        perm(cnt + 1, N)
        lst.pop()
        visited[i] = 0
        # print('after', lst, visited)


T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * (N+1)
    lst = [1]
    final = []
    
    perm(1, N)
    
    # print('final', final)

    mx_battery = 9999999999
    for path in final :
        battery = 0
        for i in range(len(path)-1) :
            # print(path, i, path[i], path[i+1])
            battery += arr[path[i]-1][path[i+1]-1]
        if mx_battery > battery :
            mx_battery = battery

    print(f'#{tc} {mx_battery}')

