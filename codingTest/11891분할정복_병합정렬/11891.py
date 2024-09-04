import sys; sys.stdin = open('sample_input.txt')

'''
알고리즘 교수님은 학생들에게 병합 정렬을 이용해 오름차순으로 정렬하는 과제를 내려고 한다.

정렬 된 결과만으로는 실제로 병합 정렬을 적용했는지 알 수 없기 때문에 다음과 같은 제약을 주었다.

N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.

병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.





정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.

알고리즘 교수님의 조건에 따라 병합 정렬을 수행하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.

5<=N<=1,000,000, 0 <= ai <= 1,000,000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,  N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력한다.
'''

'''입력
3
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
100
158 56 163 106 108 153 159 147 93 140 126 9 145 166 191 106 48 183 184 115 197 136 45 196 175 89 199 52 186 170 199 28 190 40 83 48 151 35 128 4 13 38 65 20 76 142 23 63 30 30 178 36 32 114 79 68 2 187 106 98 67 131 109 177 20 113 1 102 172 119 197 190 28 82 165 168 60 18 156 174 78 42 110 63 56 66 191 105 72 108 104 198 179 132 99 189 183 91 28 162 
'''

def merge_sort(arr) :
    if len(arr) == 1: # 종료조건 : 분할 단게에서 1개의 원소만 가질 때
        return arr
    
    mid = len(arr)//2 
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# def merge(left, right) :
#     merge_lst = []
#     while left and right :
#         if left[0] < right[0] :
#             merge_lst.append(left.pop(0))
#         else :
#             merge_lst.append(right.pop(0))

#     merge_lst.extend(left)
#     merge_lst.extend(right)
#     return merge_lst

def merge(left, right):
    global cnt
    if left[-1] > right[-1] :
        cnt += 1
        # print(left, right, cnt)

    # 두 리스트를 병합할 결과 리스트를 초기화
    result = [0] * (len(left) + len(right))
    l = r = 0  # 왼쪽 리스트와 오른쪽 리스트의 인덱스
    
    # 두 리스트를 순차적으로 비교하여 작은 값을 결과 리스트에 추가
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    # 왼쪽 리스트에 남은 요소들을 결과 리스트에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    # 오른쪽 리스트에 남은 요소들을 결과 리스트에 추가
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    


    # 병합된 결과 리스트를 반환
    return result

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    ai = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(ai)
    
    print(f"#{tc} {ans[N//2]} {cnt}")