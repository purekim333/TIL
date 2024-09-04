'''
인기 티비 프로그램 "나는 요리사 인가?"의 새 시즌이 시작한다. 이번 시즌은 기네스북에 등재될 만한 음식을 만드는 것을 목표로 진행한다.

첫 번째 에피소드에 출연하는 요리사는 전설의 요리사 김상근이고, 길이 L미터의 롤 케이크를 만들 것이다.

상근은 몇 시간동안 집중해서 케이크를 만들었고, 이제 스튜디오의 방청객 N명에게 케이크를 나누어 주려고 한다.

상근이는 롤 케이크를 펼쳐서 1미터 단위로 잘라 놓았다. 가장 왼쪽 조각이 1번, 오른쪽 조각이 L번 조각이다. 방청객은 1번부터 N번까지 번호가 매겨져 있다. 각 방청객은 종이에 자신이 원하는 조각을 적어서 낸다. 이때, 두 수 P와 K를 적어서 내며, P번 조각부터 K번 조각을 원한다는 뜻이다.

프로그램의 진행자 고창영은 1번 방청객의 종이부터 순서대로 펼쳐서 해당하는 조각에 그 사람의 번호를 적을 것이다. 이때, 이미 번호가 적혀있는 조각은 번호를 적지 못하고 넘어간다. 이런 방식을 이용해서 방청객에게 조각을 주다보니, 자신이 원래 원했던 조각을 받지 못하는 경우가 생길 수 있다.

아래 그림은 이 문제의 예제를 나타낸 것이다.



가장 많은 케이크 조각을 받을 것으로 기대한 방청객의 번호와 실제로 가장 많은 케이크 조각을 받는 방청객의 번호를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 롤 케이크의 길이 L (1 ≤ L ≤ 1000)이 주어진다. 둘째 줄에는 방청객의 수 N (1 ≤ N ≤ 1000)이 주어진다. 다음 N개 줄에는 각 방청객 i가 종이에 적어낸 수 Pi와 Ki가 주어진다. (1 ≤ Pi ≤ Ki ≤ L, i = 1..N)

출력
첫째 줄에 가장 많은 조각을 받을 것으로 기대하고 있던 방청객의 번호를 출력한다.

둘째 줄에 실제로 가장 많은 조각을 받은 방청객의 번호를 출력한다.

각 경우에 조건을 만족하는 방청객이 두 명 이상이라면 그중 번호가 가장 작은 방청객의 번호를 출력한다.
'''

'''
10
3
2 4
7 8
6 9
'''

import sys; sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    L = int(input())
    N = int(input())

    P = []
    K = []

    for _ in range(N) :
        tmp_p, tmp_k = map(int, input().split())
        P.append(tmp_p)
        K.append(tmp_k)

    cake = [0] * L + 1

    mx_think = 0
    for i in range(N) :
        start = P[i]
        end = K[i]
        think = end - start + 1
        if mx_think < think :
            mx_think = think
            mx_thinker = i+1
        man = i + 1
        for k in range(start, end+1) :
            if cake[k] == 0 :         
                cake[k] = man

    mx_get = 0
    mx_man = 0
    for man_n in range(1, N+1) :
        get = 0
        for i in range(L+1) :
            if cake[i] == man_n :
                get += 1
        if mx_get < get :
            mx_get = get
            mx_man = man_n
    print(mx_thinker)
    print(mx_man)