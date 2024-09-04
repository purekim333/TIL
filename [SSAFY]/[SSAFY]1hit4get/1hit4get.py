# 
import math

def find_point_generalized(x1, y1, x2, y2, r):
    # 1. 두 점 (x1, y1)와 (x2, y2)를 지나는 벡터
    vector_x = x2 - x1
    vector_y = y2 - y1
    
    # 2. 벡터의 크기
    magnitude = math.sqrt(vector_x**2 + vector_y**2)
    
    # 3. 단위 벡터 구하기
    unit_vector_x = vector_x / magnitude
    unit_vector_y = vector_y / magnitude
    
    # 4. r만큼 이동한 점의 좌표
    new_x = x1 + 2 * r * unit_vector_x
    new_y = y1 + 2 * r * unit_vector_y
    
    return (new_x, new_y)

# 예제 사용
x1 = -2
y1 = 3
x2 = 5
y2 = 7
r = 2

result = find_point_generalized(x1, y1, x2, y2, r)
print(f"2r 만큼 떨어져 있는 점의 좌표는: {result}")

import math

# 공과 홀의 위치 설정
balls = {
    "cue_ball": (0, 0),    # 흰색 공 위치
    "ball1": (2, 3),
    "ball2": (5, -1),
    "ball3": (-4, 4),
    "ball4": (3, -4),
    "ball5": (-3, -3)
}

holes = {
    "hole1": (-10, 5),
    "hole2": (-10, -5),
    "hole3": (0, 10),
    "hole4": (10, 5),
    "hole5": (10, -5),
    "hole6": (0, -10)
}

def distance(point1, point2):
    """ 두 점 사이의 거리 계산 """
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

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

# 공을 칠 수 있는 경로 찾기
def find_best_shot(cue_ball, balls, holes):
    best_shot = None
    min_distance = float('inf')
    
    # 칠 수 있는 공 3개를 대상으로 최적의 홀을 찾는다
    for ball_name, ball_pos in balls.items():
        for hole_name, hole_pos in holes.items():
            if is_path_clear(ball_pos, hole_pos, balls.values()):
                dist = distance(cue_ball, ball_pos) + distance(ball_pos, hole_pos)
                if dist < min_distance:
                    min_distance = dist
                    best_shot = (ball_name, hole_name)
    
    return best_shot

# 칠 수 있는 공 중에서 최적의 공과 홀을 찾기
balls_to_hit = {k: balls[k] for k in ["ball1", "ball2", "ball3"]}
best_shot = find_best_shot(balls["cue_ball"], balls_to_hit, holes)

if best_shot:
    print(f"최적의 공은 {best_shot[0]}이고, 목표 홀은 {best_shot[1]}입니다.")
else:
    print("칠 수 있는 최적의 경로가 없습니다.")
