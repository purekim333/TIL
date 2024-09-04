'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.


 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )

다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.
'''

'''
입력
3
5 
49679
5 
08271
10 
7797946543
'''

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1) :
    N = int(input())

    ai = list(input())
    pass

    # 딕셔너리로 풀기
    # card_dict = {}
    # for card in ai :
    #     if card not in card_dict.keys() :
    #         card_dict.update({card : 1})

    #     else :
    #         card_dict[card] = card_dict[card] +  1

    # mx_card = []
    # mx_card_count = 0
    # for k, v in card_dict.items() :
    #     if v >= mx_card_count :
    #         mx_card_count = v
    #         mx_card.append(int(k))

    # mx_key = 0
    # for num in mx_card :
    #     if mx_key < num :
    #         mx_key = num

    # 카운팅 정렬로 풀기
    counts = [0] * 0
    tmp = []

    for i in range(N):
        pass


    
    # print(f'#{tc} {mx_key} {mx_card_count}')
        

