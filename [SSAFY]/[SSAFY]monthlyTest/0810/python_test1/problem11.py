############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def max_adjacent_sum(matrix):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    plus_d_x = [1, 0, -1, 0]
    plus_d_y = [0, 1, 0, -1]

    max_num = 0

    for x_i, x in enumerate(matrix):
        for y_i, y in enumerate(x) :

            for i in range(4) :
                # try : 
                #     matrix[x_i][y_i] += matrix[x_i + plus_d_x[i]][y_i + plus_d_y[i]]
                # except:
                #     pass
                if (0 <= x_i + plus_d_x[i] <= len(matrix)) and (0 <= y_i + plus_d_y[i] <= len(matrix)) :
   
                    matrix[x_i][y_i] += matrix[x_i + plus_d_x[i]][y_i + plus_d_y[i]]
    for x in matrix:
        for y in x:
            if y > max_num:
                max_num = y
    return y


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

# 예시 행렬 데이터
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(max_adjacent_sum(matrix1))  # 29
print(max_adjacent_sum(matrix2))  # 25
#####################################################
