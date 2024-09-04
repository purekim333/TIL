############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장함수 len 함수를 사용하지 않습니다.
def longest_string(str_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    mx_len = 0
    mx_string = ''
    for string in str_list :
        chk_len = 0
        for index in string :
            chk_len += 1
        if chk_len > mx_len :
            mx_len = chk_len
            mx_string = string

    return mx_string
        

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 

print(longest_string(["apple", "banana", "cherry", "date"]))  # "banana"
print(longest_string(["cat", "caterpillar", "dog", "elephant"]))  # "caterpillar"
print(longest_string(["a", "ab", "abc", "abcd"]))  # "abcd"
