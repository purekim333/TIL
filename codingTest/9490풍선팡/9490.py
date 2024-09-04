import sys; sys.stdin = open('input.txt')

'''
종이 꽃가루가 들어있는 풍선이 M개씩 N개의 줄에 붙어있고, 어떤 풍선을 터뜨리면 안에 든 종이 꽃가루 개수만큼 상하 좌우의 풍선이 추가로 터지게 되는 게임이 있다.

예를 들어 풍선에 든 꽃가루가 1개씩일 때, 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.

 

NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면, 한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합 중 최대값을 출력하는 프로그램을 만드시오.

(3<=N, M<=100)

 

입력

첫 줄에 테스트케이스 수 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N과 M, 이후 N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수가 주어진다.

 

출력

#과 테스트케이스 번호, 빈칸에 이어 종이 꽃가루의 최대 개수를 출력한다.
'''

'''입력
3
3 5
2 1 1 2 2 
2 2 1 2 2 
2 2 1 1 2 
5 5
3 4 1 2 3 
3 4 1 3 2 
2 3 2 4 1 
1 4 4 1 3 
2 2 3 4 4 
5 8
1 3 4 4 4 4 3 3 
4 1 2 4 3 1 4 4 
4 1 4 4 1 4 2 1 
3 2 4 2 1 1 2 1 
4 4 1 4 4 2 2 2 
'''

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 1, 0, -1] #우 하 좌 상
    dc = [1, 0, -1, 0] #우 하 좌 상

    max_cnt = float('-inf') #꽃가루 최대 합계
    for i in range(N):  # 터트려볼 풍선의 위치
        for j in range(M):
            pang = arr[i][j]    #터트린 풍선에서 나오는 꽃가루 개수
            total = pang        
            for m in range(4) :     #주변 풍선의 꽃가루 수 / 확인할 방향 결정
                for cnt in range(1, pang+1) :   # 주변 방향으로 추가로 터지는 풍선과의 거리
                    di = i + dr[m] * cnt
                    dj = j + dc[m] * cnt
                    if 0<=di<N and 0<=dj<M :
                        # print(pang,i, j, di, dj)
                        total += arr[di][dj] #주변의 풍선에서 나오는 꽃가루 추가
            if max_cnt < total:
                max_cnt = total

    print(f'#{tc} {max_cnt}')
