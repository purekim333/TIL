############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, len 함수를 사용하지 않습니다.
def average_population(population_list):
    all = 0
    count = 0
    for num in population_list :
        all += num
        count += 1
    try : 
        average = all / count
    except :
        average = 0
    return average
    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))
#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(average_population([1000, 2000, 3000, 4000, 5000]))   # 3000.0
print(average_population([1500, 2500, 3500]))               # 2500.0
print(average_population([1234, 5678, 91011]))              # 32641.0
#####################################################