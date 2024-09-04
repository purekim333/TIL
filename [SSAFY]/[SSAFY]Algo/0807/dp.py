def fibo(n) :
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1) :
        f[i] = f[i-1] + f[i-2]

    return f[n]

def comb(n,r):
    memo = [[0] * 50 for _ in range(50)]

    for i in range(n+1) :
        for j in range(i+1) :
            if j == 0 or i == j :
                memo[i][j] = 1
            else :
                memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

    return memo[n][r]

print(comb(5,3))
print(comb(7,5))
print(comb(35,20))