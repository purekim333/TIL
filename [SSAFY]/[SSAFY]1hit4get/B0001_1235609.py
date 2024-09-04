import socket
import time
import math





# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'DAEJEON01_KIMSEUNGYUN'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.
    def my_ball_first(order) :
        targetBall = []
        if order == 1 : #선공
            print('선공입니다')
            for i in range(1,4,2):
                targetBall.append(i)
                targetBall.append(i)
        return targetBall
    
    def my_ball_second(order) :
        targetBall = []
        if order == 2: #후공
            print('후공입니다.')
            for k in range(2, 5, 2) :
                targetBall.append(k)
                targetBall.append(k)
        return targetBall

    def get_distance(x1, y1, x2, y2) :
        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return dist

    def find_hole(targetBall_num, Holes, whiteball_x, whiteball_y):
        target_x = balls[targetBall_num][0]
        target_y = balls[targetBall_num][1]
        hole_x = 0
        hole_y = 0
        ## 1사분면일 경우
        if target_x > whiteball_x and target_y > whiteball_y :
            if target_x < 127 :
                hole_x = Holes[4][0]
                hole_y = Holes[4][1]
            else :
                hole_x = Holes[5][0]
                hole_y = Holes[5][1]

        #2사분면
        if target_x < whiteball_x and target_y > whiteball_y :
            if target_x < 127 :
                hole_x = Holes[1][0]
                hole_y = Holes[1][1]
            else :
                hole_x = Holes[4][0]
                hole_y = Holes[4][1]
        #3사분면
        if target_x < whiteball_x and target_y < whiteball_y :
            if target_x < 127 :
                hole_x = Holes[0][0]
                hole_y = Holes[0][1]
            else :
                hole_x = Holes[3][0]
                hole_y = Holes[3][1]
        #4사분면
        if target_x > whiteball_x and target_y < whiteball_y :
            if target_x < 127 :
                hole_x = Holes[3][0]
                hole_y = Holes[3][1]
            else :
                hole_x = Holes[2][0]
                hole_y = Holes[2][1]

        # min_dist = 254
        # for hole in Holes :
        #     hole_x = hole[0]
        #     hole_y = hole[1]

        #     tmp_dist = get_distance(target_x, target_y, hole_x, hole_y)
        #     if min_dist > tmp_dist :
        #         min_dist = tmp_dist
        #         
        # print(min_dist, final_hole)

        final_hole = (hole_x, hole_y)
        return final_hole

    def get_unit_vector(x1, y1, x2, y2) :
        vector_x = x2 - x1
        vector_y = y2 - y1

        vector_length = get_distance(x1, y1, x2, y2)

        unit_x = vector_x / vector_length
        unit_y = vector_y / vector_length

        return unit_x, unit_y

    def get_final_destination(targetBall_num, targetHole, r) :
        targetball_x = balls[targetBall_num][0]
        targetball_y = balls[targetBall_num][1]

        hole_x, hole_y = targetHole

        unit_x, unit_y = get_unit_vector(hole_x, hole_y, targetball_x, targetball_y)

        print('단위벡터', unit_x, unit_y)
        new_x = targetball_x + 2 * r * unit_x
        new_y = targetball_y + 2 * r * unit_y

        return new_x, new_y
    
    def is_path_clear(start, end, obstacles):
        """ 
        시작점과 끝점 사이에 장애물이 있는지 확인 
        이 함수는 직선 경로 상에 장애물이 있는지를 간단히 확인하는 방식입니다.
        """
        for obstacle in obstacles:
            # 선형 방정식을 이용해 장애물이 경로 상에 있는지 판단
            dist = abs((end[1] - start[1]) * obstacle[0] - 
                    (end[0] - start[0]) * obstacle[1] +
                    end[0] * start[1] - 
                    end[1] * start[0]) / distance(start, end)
            if dist < 1:  # 임의의 임계값, 필요 시 조정 가능
                return False
        return True


    r = 5.55/2  #반지름
    c = 1.95      #홀 위치
    HOLES = [[0 + c, 0 + c], [127, 0 + c], [254 - c, 0 + c], [0 + c, 127 - c], [127, 127 - c], [254 - c, 127 - c]]
    
    targetBall = []
    if order == 1:
        targetBall = my_ball_first(order)
        targetBall.append(5)

    else :
        targetBall = my_ball_second(order)
        targetBall.append(5)
    
    targetBall_num = targetBall[0] #몇 번 공을 칠것이다 결정

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    targetHole = find_hole(targetBall_num, HOLES, whiteBall_x, whiteBall_y)
    targetHole_x, targetHole_y = targetHole
    print('targetHole', targetHole_x, targetHole_y)


    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    # targetBall_x = balls[targetBall_num][0]
    # targetBall_y = balls[targetBall_num][1]

    targetBall_x, targetBall_y = get_final_destination(targetBall_num, targetHole, r)
    # targetBall_x, targetBall_y = balls[targetBall_num][0], balls[targetBall_num][1]
    print('targetpoint' , targetBall_x, targetBall_y)

    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    radian = math.atan(width / height) if height > 0 else 0
    angle = 180 / math.pi * radian
    print('angle', angle)
    
    # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
    if whiteBall_x == targetBall_x:
        if whiteBall_y < targetBall_y:
            angle = 0
        else:
            angle = 180
    elif whiteBall_y == targetBall_y:
        if whiteBall_x < targetBall_x:
            angle = 90
        else:
            angle = 270

    # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
    if whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:
        radian = math.atan(width / height)
        angle = 360 - (180 / math.pi * radian)
        print('2사 angle', angle)

    # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    if whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(width / height)
        angle = (180 / math.pi * radian) + 180
        print('3사 angle', angle)
    
    # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 90
        print('4사 angle', angle)
        
    # distance: 두 점(좌표) 사이의 거리를 계산
    distance = math.sqrt(width**2 + height**2)
    print(width,distance)

    # power: 거리 distance에 따른 힘의 세기를 계산
    # power = distance * 0.45  #거리의 몇 배만큼의 세기
    power = 36  #거리의 몇 배만큼의 세기

    

    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')




