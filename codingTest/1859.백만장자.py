# import sys
# sys.stdin = open("사전학습\input.txt", "r")

# T = sys.stdin
# for text in T :
#     print(text,"\n")
# for text in T :
#     print(text)
# T = int(input())
# # # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     print(T)

total_num = int(input())
price = []

for i in range(total_num) :
    price.append(int(input("{}번쨰 수를 입력해주세요 : ".format(i))))

max_num = price[-1]
for k in price :
    if k > max_num :
        max_num = k
        
