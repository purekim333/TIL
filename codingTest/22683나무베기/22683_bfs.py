import sys
sys.stdin = open('sample_input.txt')
from heapq import heappush, heappop

# 상우하좌
dxy = ((0, -1), (1, 0), (0, 1), (-1, 0))


def bfs():
    cost, cut, dir, x, y = 0, 0, 0, sx, sy
    hq = [(cost, dir, x, y, cut)]
    visited[cut][y][x] = cost  # 처음 시작점은 비용 0으로 설정

    while hq:
        cost, dir, x, y, cut = heappop(hq)          # cost: 조작 횟수, dir: 방향, cut: 지금까지 나무를 자른 횟수

        if x == ex and y == ey:
            return cost

        r_dir = (dir + 1) % 4       # 1
        l_dir = (dir - 1) % 4       # 3
        d_dir = (dir + 2) % 4       # 2

        for d in (dir, r_dir, l_dir, d_dir):
            n_cost = cost + 1
            if d == r_dir or d == l_dir:
                n_cost += 1
            elif d == d_dir:
                n_cost += 2

            nx = x + dxy[d][0]
            ny = y + dxy[d][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 나무를 자르는 경우
            if grid[ny][nx] == 'T' and cut < K and visited[cut + 1][ny][nx] > n_cost:
                visited[cut + 1][ny][nx] = n_cost
                heappush(hq, (n_cost, d, nx, ny, cut + 1))
            # 나무를 자르지 않는 경우
            elif grid[ny][nx] != 'T' and visited[cut][ny][nx] > n_cost:
                visited[cut][ny][nx] = n_cost
                heappush(hq, (n_cost, d, nx, ny, cut))

    return -1


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    grid = []
    sx, sy, ex, ey = 0, 0, 0, 0

    # 입력 받으면서 시작 점 끝점 저장
    for i in range(N):
        row = input()
        grid.append(row)
        for j in range(N):
            if row[j] == 'X':
                sx, sy = j, i
            if row[j] == 'Y':
                ex, ey = j, i


    # visited 배열이 3차원인 이유
    # K=2일 때 0번 짜른 visited 1번 짜른 visited 2번 짜른 visited
    visited = [[[float('inf')] * N for _ in range(N)] for _ in range(K + 1)]
    answer = bfs()
    for i in range(K+1):
        print(i)
        for j in range(N):

            print(*visited[i][j])
        print('===============')

    print(f'#{tc} {answer}')

"""
풀이 방법 - 다익스트라 알고리즘 응용
기존 다익스트라 알고리즘은 거리의 가중치가 주어줬다면 해당 문제는 조작횟수가 가중치라고 생각하면 됨 
"""