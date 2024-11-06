from libs._bridge import init, submit, close

NICKNAME = '기본코드'
game_data = init(NICKNAME)


# 입력 데이터 분류
char_to_int = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
map_data = [[]]  # 맵 정보. 예) map_data[0][1] - [0, 1]의 지형/지물
allies = {}  # 아군 정보. 예) allies['A'] - 플레이어 본인의 정보
enemies = {}  # 적군 정보. 예) enemies['X'] - 적 포탑의 정보
codes = []  # 주어진 암호문. 예) codes[0] - 첫 번째 암호문

# 입력 데이터를 파싱하여 변수에 저장
def parse_data(game_data):
    # 입력 데이터를 행으로 나누기
    game_data_rows = game_data.split('\n')
    row_index = 0

    # 첫 번째 행 데이터 읽기
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0])  # 맵의 세로 크기
    map_width = int(header[1])  # 맵의 가로 크기
    num_of_allies = int(header[2])  # 아군의 수
    num_of_enemies = int(header[3])  # 적군의 수
    num_of_codes = int(header[4])  # 암호문의 수
    row_index += 1

    # 기존의 맵 정보를 초기화하고 다시 읽어오기
    map_data.clear()
    map_data.extend([[ '' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, map_width):
            map_data[i][j] = col[j]
    row_index += map_height

    # 기존의 아군 정보를 초기화하고 다시 읽어오기
    allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0)
        allies[ally_name] = ally
    row_index += num_of_allies

    # 기존의 적군 정보를 초기화하고 다시 읽어오기
    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0)
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    # 기존의 암호문 정보를 초기화하고 다시 읽어오기
    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])

# while 반복문: 배틀싸피 메인 프로그램과 클라이언트(이 코드)가 데이터를 계속해서 주고받는 부분
while game_data is not None:
    # 자기 차례가 되어 받은 게임정보를 파싱
    print(f'----입력데이터----\n{game_data}\n----------------')
    parse_data(game_data)

    # 파싱한 데이터를 화면에 출력하여 확인
    print(f'\n[맵 정보] ({len(map_data)} x {len(map_data[0])})')
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            print(f'{map_data[i][j]} ', end='')
        print()

    print(f'\n[아군 정보] (아군 수: {len(allies)})')
    for k, v in allies.items():
        if k == 'A':
            print(f'A (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 대전차 포탄: {v[3]}개')
        elif k == 'H':
            print(f'H (아군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (아군 탱크) - 체력: {v[0]}')

    print(f'\n[적군 정보] (적군 수: {len(allies)})')
    for k, v in enemies.items():
        if k == 'X':
            print(f'H (적군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (적군 탱크) - 체력: {v[0]}')

    print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
    for i in range(len(codes)):
        print(codes[i])

    # ================================================================================================
    # =====================================코드는 여기부터 수정=========================================
    # ================================================================================================
    # 가로, 세로 크기 변수로
    ROW, COL = len(map_data), len(map_data[0])

    # ================================================================================================
    # BFS
    from collections import deque
    def BFS(cur_r, cur_c):
        queue = deque([(cur_r, cur_c, 0)])      # 현재 행, 현재 열, 움직인 칸 개수
        visited = [[0] * COL for _ in range(ROW)]

        while queue:
            cur_r, cur_c, cnt = queue.popleft()
            visited[cur_r][cur_c] = 1

            if map_data[cur_r][cur_c] == 'X':
                return cnt

            for k in range(4):
                nr = cur_r + dr[k]
                nc = cur_c + dc[k]
                if 0 <= nr < ROW and 0 <= nc < COL and not visited[nr][nc] and map_data[nr][nc] != 'R':
                    queue.append((nr, nc, cnt+1))

    # ================================================================================================
    # 암호 해독 방법 : 알파벳 순서에서 7칸 뒤로 가기
    # 단순히 ord(알파벳)+7 하면 안됨 (ord('Z') + 7 같은 경우도 생각해야 하기 때문)
    # 알파벳은 총 26개이므로 26으로 나눈 나머지를 활용하면 됨
    def decoding(code):
        decoded = ''
        for ch in code:
            decoded += chr((ord(ch) - ord('A') + 7) % 26 + ord('A'))
        return decoded

    #print(decoding('BEHOXLLTYR'))

    # ================================================================================================
    # 탱크의 동작을 결정하기 위한 알고리즘을 구현하고 원하는 커맨드를 output 변수에 담기
    # 코드 구현 예시: '아래쪽으로 전진'하되, 아래쪽이 지나갈 수 있는 길이 아니라면 '오른쪽로 전진'하라

    output = 'S'  # 알고리즘 결괏값이 없을 경우를 대비하여 초기값을 S로 설정

    # 방향 리스트
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]   # 상 우 하 좌
    dirs = ['U','R','D','L']

    # 내 현재 위치, 목표 위치 찾기
    my_position = (-1, -1)
    goal_position = (-1, -1)
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] == 'A':
                my_position = (i, j)
            if map_data[i][j] == 'X':
                goal_position = (i, j)

    # ================================================================================================
    # 근처에 포탑 있는지 확인
    if abs(my_position[0] - goal_position[0]) + abs(my_position[1] - goal_position[1]) == 1:  # 1칸 이내 근접
        # 목표 방향으로 총구를 돌림
        if my_position[0] < goal_position[0]:
            output = 'D F M'  # 아래쪽으로 돌리고 폭발
        elif my_position[0] > goal_position[0]:
            output = 'U F M'  # 위쪽으로 돌리고 폭발
        elif my_position[1] < goal_position[1]:
            output = 'R F M'  # 오른쪽으로 돌리고 폭발
        elif my_position[1] > goal_position[1]:
            output = 'L F M'  # 왼쪽으로 돌리고 폭발

    # 근처에 포탑 없으면
    else:
        # 4방향 다 가보고 어디로 가는게 최고의 판단인지 결정
        four_dir_min_dist = [1e9] * 4
        for k in range(4):
            nr = my_position[0] + dr[k]
            nc = my_position[1] + dc[k]
            if 0 <= nr < ROW and 0 <= nc < COL and map_data[nr][nc] != 'R':
                four_dir_min_dist[k] = BFS(nr, nc)

        # 거리가 최소인 방향
        dir = four_dir_min_dist.index(min(four_dir_min_dist))
        output = dirs[dir] + ' A'

    # ================================================================================================
    # while 문의 끝에는 다음 코드가 필수로 존재하여야 함
    # output에 담긴 값은 submit 함수를 통해 배틀싸피 메인 프로그램에 전달
    game_data = submit(output)


# 반복문을 빠져나왔을 때 배틀싸피 메인 프로그램과의 연결을 완전히 해제하기 위해 close 함수 호출
close()