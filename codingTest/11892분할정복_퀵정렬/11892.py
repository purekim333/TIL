import sys;sys.stdin = open('sample_input.txt')

'''
퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.

5<=N<=1,000,000, 0 <= ai <= 1,000,000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, , N/2번 원소를 출력한다.
'''

def hoare_partition(left, right) :
    pivot = arr[left]
    i = left + 1
    j = right

    while i <= j :
        while i <= j and arr[i]<= pivot :
            i += 1
        while i <= j and arr[j] >= pivot :
            j -= 1
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

def quick_sort(left, right) :
    if left < right:
        pivot = hoare_partition(left, right)

        quick_sort(left, pivot-1)
        quick_sort(pivot + 1, right)

        


T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    arr = list(map(int, input().split()))

    # print(N, arr)
    quick_sort(0, len(arr) -1)
    print(f'#{tc}', arr[N//2])

