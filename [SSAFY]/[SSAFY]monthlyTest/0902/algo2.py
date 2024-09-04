import sys; sys.stdin = open('algo2_sample_in.txt')

def tree(node_num, N) :
    global ans
    if node_num > N :
        return ''

    tree(node_num * 2, N)
    ans += node[node_num]
    tree(node_num * 2 + 1, N)

    # ans += l + r
    # print(node_num, l, r, node[node_num], ans)

    # return node[node_num]

T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    ch = input()
    asci = 0
    result = ''
    for c in ch :
        asci = ord(c)
        # print(c, asci, bin(asci))
        bin_ch = bin(asci)[2:]
        # print(c, asci, bin_ch)
        # bin_ch = bin_ch[::-1]
        node = [0] * (len(bin_ch)+1)

        for i in range(len(bin_ch)):
            node[i+1] = bin_ch[i]

        # print(c, node)
        ans = ''
        tree(1, len(bin_ch))
        # ans += node[1]
        result += ans + ' '

    print(f'#{tc} {result}')





