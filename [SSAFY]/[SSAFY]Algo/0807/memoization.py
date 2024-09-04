def fibo(n) :
    global memo
    if n >= 2 and memo[n] == 0 :
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

n = 7
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1

fibo(n)
print(memo) # [0, 1, 1, 2, 3, 5, 8, 13]