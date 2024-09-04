import sys; sys.stdin = open('sample_input.txt')

'''
16진수 1자리는 2진수 4자리로 표시된다.

N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.

단, 2진수의 앞자리 0도 반드시 출력한다.

예를 들어 47FE라는 16진수를 2진수로 표시하면 다음과 같다.

0100011111111110


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 자리 수 N과 N자리 16진수가 주어진다. 1<=N<=100
'''

T = int(input())

for tc in range(1, T+1) :
    N, arr = input().split()
    N = int(N)
    # lst = list(lst)

    bin_str = []
    for ch in arr:
    # ch => 정수로 변환
    # if '0' <= ch <= '9':
    #     num = ord(ch) - ord('0')
    # else:
    #     num = 10 + ord(ch) - ord('A')
        num = int(ch, 16)
        bin_str.append(1 if num & 8 else 0) # 8 == 1 << 3
        bin_str.append(1 if num & 4 else 0) # 4 == 1 << 2
        bin_str.append(1 if num & 2 else 0) # 2 == 1 << 1
        bin_str.append(1 if num & 1 else 0) # 1 == 1 < 0
    print(f'#{tc} ', *bin_str, sep='')


