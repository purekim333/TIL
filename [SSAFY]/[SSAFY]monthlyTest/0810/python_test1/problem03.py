############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 count 를 사용하지 않습니다.
def count_treasures(treasure_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    treasure_dict = {}
    for treasure in treasure_list :
        count = 1
        if treasure in treasure_dict.keys() : 
            count += treasure_dict[treasure]
        treasure_dict.update({treasure : count})
    return treasure_dict

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(count_treasures(["gold", "silver", "diamond", "gold", "silver"]))  # {'gold': 2, 'silver': 2, 'diamond': 1}
print(count_treasures(["pearl"]))  # {'pearl': 1}
#####################################################
