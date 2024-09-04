'''
주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.

Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition.

위 문장에서 ti 를 검색하면, 답은 4이다.

[제약 사항]

총 10개의 테스트 케이스가 주어진다.

문장의 길이는 1000자를 넘어가지 않는다.

한 문장에서 검색하는 문자열의 길이는 최대 10을 넘지 않는다.

한 문장에서는 하나의 문자열만 검색한다. 

[입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 찾을 문자열, 그 다음 줄에는 검색할 문장이 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
'''
'''
입력
1
ti
Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasics ...
2
ing
Thedoublehelixformsthestructuralbasisofsemi-conservativeDNAreplication.1,2Less ...
...
'''

import sys; sys.stdin = open('test_input.txt', encoding='utf-8')

for _ in range(10) :
    tc = int(input())

    p = input()
    t = input()

    cnt = 0
    for i in range(len(t)-len(p)+1) :
        for j in range(len(p)) :
            found = True
            if p[j] != t[i+j] :
                found = False
                break

        if found :
            cnt += 1        


    print(f'#{tc} {cnt}')