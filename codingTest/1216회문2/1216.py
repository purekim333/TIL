'''
"기러기" 또는 "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.
 

 

위와 같은 글자 판이 주어졌을 때, 길이가 가장 긴 회문은 붉은색 테두리로 표시된 7칸짜리 회문이다.

예시의 경우 설명을 위해 글자판의 크기가 100 x 100이 아닌 8 x 8으로 주어졌음에 주의한다.

[제약사항]

각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.

글자 판은 무조건 정사각형으로 주어진다.

ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.

가로, 세로 각각에 대해서 직선으로만 판단한다. 즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다. 
 


[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 길이를 출력한다.
'''
'''
입력
1
CCBBCBAABCCCBABCBCAAAACABBACCCCACAABCBBACACAACABCBCCB...
ACBAAAACCACCCBAACAAABACACCABCBCBABBBACBABCAACCBCCACBC...
CCCACCBCBACBACBCABAABABCCAAAACCCCCBBAABBCCBCCCABBACAC...
CABACBCBBCBABACABBBBBBABBCABCBCBCAABCBCCCBABACCCCABBA...
BCCBCCACCBCBCABBBCCABAACACCBCCCBCCACCBBCBCCCBBCCBACBC...
BBBBCBBAACABACCBCBCCABBBBCCAABCBBCACCBBCAAAABABABBABB...
ABBAACCCACBBABBABCCCABABCACABABACCCBACACABCBCCCBABCCC...
ABBBBAABCAACCBACBBAACACABCABACBAABCAABBCCCCCCACBCCCCA...
ACCACABABBACBBAACCBBACBBCCACCACCABCCBABABBBACBACBAABC...
BABACACCABCAACBAABCCACCACBCCAABBCBAABABAACAAAAAACCCBC...
...
2
CBBABBACCAACCCAABABAACCABCBBCCABABBBBBCCACBCCCCBBBAAC...
BBBCBACAAABAACACBCAABBAAABCABBBCAAACBAABCAAAAACBABBAB...
CAAAABCAABAACCBBABCCCACABABACBCCBCCBABABBCCCBCBACAAAC...
BBBACBBBBBAACBBCBABBCBAABACCCBBBBCCCBBBCABCABCAABCBCA...
ABBBBAABCBACCACBBCBBAABABCBCCAAABBCAAABBAABBCACABAABA...
ABCBACAAACCCAAABCACABBAABBCAACCBABCCACBABBBABAABAACBB...
ACACABCBAAACCACABABBCABCBABAAABCBCCABABCCAACACBCBABCA...
ACCBACACCAAAABABACABABBBBABBAABABBBBACBACABABACACACAA...
AAACCCCCBCAACCCCCAAAACBCACBBABBBBBABABBCCCCBBAACCBBCB...
CCABCCBBCAAAACACBBBBAAAACABACABCCCBACBABBACCAABAAACAB...
'''

import sys; sys.stdin = open('input.txt')

for _ in range(10) :
    tc = int(input())

    arr = [input() for _ in range(100)]

    N = 100

    # M = 1 ~ 101

    #가로탐색
    for M in range(1, 101) :
        for r in range(100) :
            for c in range(100-M +1) :
                    e = c + M - 1
                    for i in range(M//2) :
                        if arr[r][c+i] != arr[r][e-i] :
                             break
                        
                    else :
                        mx_M = M

    #세로탐색
    for M in range(1, 101) :
        for c in range(100) :
            for r in range(100-M +1) :
                    e = r + M - 1
                    for i in range(M//2) :
                        if arr[r+i][c] != arr[e-i][c] :
                             break
                        
                    else :
                        if mx_M < M:
                             mx_M = M

    print(f'#{tc} {mx_M}')