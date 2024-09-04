
arr = [10, 20, 30]
N = len(arr)

# while i < 3 :
#     print('Hello!' )
#     i += 1
bits = [0] * N
subset = []
# 재귀 -> 반복
def backtrack(k, n) :
    if k == n: #종료조건 설정하기
        global cnt
        cnt += 1
        print(cnt, bits)
        print(subset)
    # 반복할 내용은 출력하기
    else :
        bits[k] = 1
        subset.append(arr[bits[k]])
        backtrack(k + 1, n)
        subset.pop()

        bits[k] = 0
        backtrack(k + 1, n)

# i가 재귀의 depth를 컨트롤
# k가 재귀의 종료조건 (i가 k와 같아질 때까지)
cnt = 0 #전역변수
backtrack(0, 3)
