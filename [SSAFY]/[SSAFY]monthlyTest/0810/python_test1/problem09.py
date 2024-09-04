############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_number_sum(word):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    word = word + 'a'
    num = ''
    num_list = []
    for i, ch in enumerate(word) :
        if ch.isdigit() == True :
            num += ch
            

        elif ch.isdigit() == False:
            if num != '' :
                num_list.append(int(num))
                num = ''

    return sum(num_list)



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_number_sum('ab123cd45ef6'))     # 174
print(calculate_number_sum('0a1s2d3f4'))        # 10
print(calculate_number_sum('ssafy10gi2good4560')) # 4572
#####################################################
