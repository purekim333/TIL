'''
숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.

"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.

예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.

[입력]

입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.

그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백 문자 후 테스트 케이스의 길이가 주어진다.

테스트 케이스의 길이란, 문자열의 글자수가 아닌 단어의 갯수를 말한다.

그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다.
'''

'''
입력
10
#1 7041
SVN FOR ZRO NIN FOR EGT EGT TWO FOR FIV FIV ONE SVN ONE ONE FIV TWO SVN SIX ONE FOR TWO THR TWO TWO ONE SIX EGT FIV SVN SIX ONE EGT NIN TWO SVN NIN FIV FOR THR ONE TWO THR THR FOR ONE ONE THR EGT SVN FOR TWO SVN SVN NIN THR ONE NIN EGT SIX FIV ZRO TWO EGT SIX ZRO TWO FOR EGT SIX FIV ZRO NIN ZRO ZRO SIX ONE THR EGT NIN THR FOR FOR SIX ZRO SIX SIX ONE...
#2 7778
EGT ONE THR SIX ZRO ZRO NIN FIV FOR EGT SVN FOR NIN NIN EGT THR EGT FIV TWO ONE FIV THR ONE SIX SVN THR ZRO FIV TWO TWO ONE FIV ZRO TWO SIX TWO EGT THR SIX SVN FOR FIV THR SVN SVN EGT EGT FOR ZRO THR FIV EGT NIN THR ONE SVN ZRO NIN THR THR FIV SVN THR SIX FOR NIN FOR ZRO ZRO NIN SVN EGT SIX FIV TWO TWO THR FIV THR SVN NIN ONE ZRO FIV ZRO NIN THR SIX ...
...
'''

import sys 
sys.stdin = open('GNS_test_input.txt')

T = int(input())

number_book = {
    'ZRO' : 0,
    'ONE' : 1,
    'TWO' : 2,
    'THR' : 3,
    'FOR' : 4,
    'FIV' : 5,
    'SIX' : 6,
    'SVN' : 7,
    'EGT' : 8,
    'NIN' : 9
}

number_book2 = {
    0 : 'ZRO',
    1 : 'ONE',
    2 : 'TWO',
    3 : 'THR',
    4 : 'FOR',
    5 : 'FIV',
    6 : 'SIX',
    7 : 'SVN',
    8 : 'EGT',
    9 : 'NIN'
}

for tc in range(1, T+1) :
    testcase, test_len = input().split()
    arr = list(input().split())

    test_len = int(test_len)

    for i in range(test_len) :
        arr[i] = number_book[arr[i]]
        

    for j in range(test_len) :
        mn_index = i
        for k in range(j+1, test_len) :
            if arr[mn_index] > arr[k] :
                mn_index = k
        arr[j], arr[mn_index] = arr[mn_index], arr[j]


    for i in range(test_len) :
        arr[i] = number_book2[arr[i]]

    print(testcase)
    print(*arr)


