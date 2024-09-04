############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_days_to_fill_tank(tank_capacity, fill_amount, evaporation_amount):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    day = 0
    left_water = 0
    while left_water < tank_capacity:
        left_water += fill_amount
        day += 1
        if left_water >= tank_capacity :
            break
        left_water -= evaporation_amount
    return day

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))
print(calculate_days_to_fill_tank(100,100,100))
#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_days_to_fill_tank(100, 20, 5))  # 7
print(calculate_days_to_fill_tank(1000, 100, 10))  # 11
print(calculate_days_to_fill_tank(100, 10, 1))  # 11
#####################################################
