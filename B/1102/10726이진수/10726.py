import sys; sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # for n in range(N):
    #     flag = False
    #     if M>>n & 1:
    #         ans = 'ON'
    #     else :
    #         ans = 'OFF'
    #         break
    if ((1<<N)-1) == (M&((1<<N) -1)):
        ans = 'ON'
    else:
        ans = 'OFF'

    print(f'#{tc}',ans)
