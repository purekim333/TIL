'''
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
 

예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
 

테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

'''
입력
3
3 6
5 15
5 10
'''
import sys
sys.stdin = open('sample_input.txt')

def match_index(arr, count) :
    set_lst = []
    for index in range(get_count(arr)) :
        if count[index] == 1:
            set_lst.append(arr[index])
    return set_lst
    
def get_sum(arr):
    ls_sum = 0
    for num in arr :
        ls_sum += num
    return ls_sum
    
def get_count(arr) :
    tmp_count = 0
    for _ in arr :
        tmp_count += 1
    return tmp_count

def get_answer(arr) :
    answer = 0
    for element in arr:
        if get_count(element) == N and get_sum(element) == K :
            answer += 1
    return answer

# def drop_the_beat(length, arr, num) :
#     subset_lst = []
#     for bit in range(2) :
#         arr[num] = bit

T = int(input())

for tc in range(1, T+1) :
    N, K = map(int, input().split())

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    count = [0] * 12

    subset_lst = []
    for a in range(2) :
        count[0] = a
        for b in range(2) :
            count[1] = b
            for c in range(2) :
                count[2] = c
                for d in range(2) :
                    count[3] = d
                    for e in range(2) :
                        count[4] = e
                        for f in range(2) :
                            count[5] = f
                            for g in range(2) :
                                count[6] = g
                                for h in range(2) :
                                    count[7] = h
                                    for i in range(2) :
                                        count[8] = i
                                        for j in range(2) :
                                            count[9] = j
                                            for k in range(2) :
                                                count[10] = k
                                                for l in range(2) :
                                                    count[11] = l

                                                    # set_lst = []
                                                    # for index in range(12) :
                                                    #     if count[index] == 1 :
                                                    #         set_lst.append(A[index])
                                                    # subset_lst.append(set_lst)

                                                    subset = match_index(A, count)
                                                    subset_lst.append(subset)
    
    
    answer = get_answer(subset_lst)
    print(f'#{tc} {answer}')

