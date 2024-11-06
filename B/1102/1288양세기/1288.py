import sys; sys.stdin=open('input.txt')

T = int(input())

for tc in range(1, T+1):
	N = input()
	int_N = int(N)
	up = 1
	count = 0
	doc = bin(1<<11)

    while True :
        count += 1
        n = N
        for k in n:
    	    digit = int(k)
        doc = bin(doc | (1<<digit))
        up += 1
        n = str( int_N * up)
	print(doc)