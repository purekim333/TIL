# 교환을 통한 순열 생성
# arr = ['A', 'B', 'C', 'D']
# N = len(arr)

# for i in range(0, N) :
#     arr[0], arr[i] = arr[i], arr[0]
#     print(arr)

#예상 출력 결과
#      -> ABCD
# ABCD -> BACD
#      -> CBAD
#      -> DBCA

# #실제 출력 결과
# ['A', 'B', 'C', 'D']
# ['B', 'A', 'C', 'D']
# ['C', 'A', 'B', 'D']
# ['D', 'A', 'B', 'C']

# 이유 -> 이전에 출력한 리스트에서 바로 교환이 이루어지기 때문에
# 원래대로 되돌려 주는 작업이 필요한다. (백트래킹)

# arr = ['A', 'B', 'C']
# N = len(arr)

# for i in range(0, N) :
#     arr[0], arr[i] = arr[i], arr[0]
#     #+++++++++++++++++++++++++++++++++++
#     for j in range(1, N):
#         arr[1], arr[j] = arr[j], arr[1]
#         #+++++++++++++++++++++++++++++++++++
#         for k in range(2, N) :
#             arr[2], arr[j] = arr[j], arr[2]
#             print(arr)
#             arr[2], arr[j] = arr[j], arr[2]
#         #+++++++++++++++++++++++++++++++++++
#         arr[1], arr[j] = arr[j], arr[1] # 백트래킹 
#     #+++++++++++++++++++++++++++++++++++ 
#     arr[0], arr[i] = arr[i], arr[0] # 백트래킹


# def backtrack(k, n) :
#     if k == n :
#         print(arr)
#     else :
#         for i in range(k, N) :
#             arr[k], arr[i] = arr[i], arr[k]
#             backtrack(k+1, n)
#             arr[k], arr[i] = arr[i], arr[k]

# backtrack(0, N)

#============================
arr = [1, 2, 3]
N = len(arr)
visit = [0] * N  # 요소의 선택 여부 저장
order = [0] * N  # 실제 순열의 순서를 저장

# =============================================
# 1. 반복 구조
for i in range(N):      # 첫번째 요소 선택
    if visit[i]: continue
    order[0] = arr[i]
    visit[i] = 1
    #----------------------------------------------
    for j in range(N):  # 두번째 요소 선택
        if visit[j]: continue
        order[1] = arr[j]
        visit[j] = 1
        #------------------------------------------
        for k in range(N): # 세번째 요소 선택
            if visit[k]: continue
            order[2] = arr[k]
            visit[k] = 1
            print(order)
            visit[k] = 0
        #------------------------------------------
        visit[j] = 0
    #------------------------------------------
    visit[i] = 0

# =============================================
# 2. 재귀 구조
def perm(k, N):
    if k == N:
        print(order)
    else:
        for i in range(N):  # 첫번째 요소 선택
            if visit[i]: continue
            order[k] = arr[i]
            visit[i] = 1
            #---------------------
            perm(k + 1, N)
            #---------------------
            visit[i] = 0
perm(0, N)
