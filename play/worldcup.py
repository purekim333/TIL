import random
import time

def get_random_index(player_list) :
    num = random.randint(0, len(player_list) -1)
    return num

def dugu() :
    print('두구두구두구두구두구두구두구두구')
    time.sleep(1)

def remove_guy(player, player_list) :
    for i, man in enumerate(player_list):
        if man == player :
            player_list = player_list[:i] + player_list[i+1:]
    return player_list

def chk_bujeon(player_list) :
    if len(player_list) % 2 == 1 :
        lucky_guy_i = get_random_index(player_list)
        print('시작하기에 앞서 부전승을 뽑겠습니다.')
        time.sleep(1)
        print('부전승 행운의 인물은~?')
        time.sleep(1)
        print('부전승 : ', player_list[lucky_guy_i], '!!!')
        return player_list[lucky_guy_i]
    
def get_two_player(player_list) :
    player1 = player_list[get_random_index(player_list)]
    player_list = remove_guy(player1, player_list)
    player2 = player_list[get_random_index(player_list)]
    player_list = remove_guy(player2, player_list)
    return player1, player2, player_list
    
def worldCup(player_list) :
    next_player_list = []
    lucky_guy = chk_bujeon(player_list)
    if type(lucky_guy) == type('a') :
        next_player_list.append(lucky_guy)
    player_list = remove_guy(lucky_guy, player_list)

    while player_list :
        player1, player2, player_list = get_two_player(player_list)

        while True:
            print(f'둘 중에 한명만 골라주세용 : {player1} vs {player2}')
            while True :
                winner_num = input('winner (1 or 2) : ')
                if winner_num == '1' :
                    winner = player1
                    break
                elif winner_num == '2' :
                    winner = player2
                    break
                else :
                    print('혹시 똑바로 골라주겠어?')

            if winner == player1 or winner == player2 :
                print(f'{winner} 확인 ㅋㅋ')
                next_player_list.append(winner)
                time.sleep(1)
                break
            else :
                print('혹시 똑바로 골라주겠어?')
                time.sleep(1)

    return next_player_list

def before_final(player_list) :
    while True :
        gang = len(player_list)
        print('===========================')
        print(f'{gang}강 시작합니다! 섞는중...')
        print('===========================')
        print('후보 :' , *player_list)
        player_list = worldCup(player_list)
        if len(player_list) == 2 :
            break

    return player_list

def final(player_list) :
    print('===========')
    print('대망의 결승 !')
    print('===========')
    dugu()
    
    player1 = player_list[0]
    player2 = player_list[1]
    
    
    
    while True :
        print(f'둘 중에 한명만 골라주세용 : {player1} vs {player2}')
        winner_num = input('winner (1 or 2) : ')
        if winner_num == '1' :
            winner = player1
            break
        elif winner_num == '2' :
            winner = player2
            break
        else :
            print('올바르게 입력해주세요')

    print(f'우승자는 {winner} !!!')

if __name__=="__main__":
    player_list = ['!*김승윤*!', '김민정', '김지훈', '박상호', '서영광', '김선진', '노승혜', '류현', '김태열', '오승열', '이가영', '임현빈',
                   '정다인', '조기흠', '조현준', '최담천', '최이화', '민태홍', '편정웅', '김한길', '이현희', '김혜민']
    
    # player_list_m = ['!*김승윤*!', '김지훈', '박상호', '서영광', '김선진', '김태열', '오승열', '임현빈',
    #                 '조기흠', '조현준', '최담천', '민태홍', '편정웅', '김한길']

    # player_list_w = ['김민정', '노승혜', '류현', '이가영', 
    #                '정다인', '최이화', '이현희', '김혜민']

    name = input("본인 이름을 적어주세요 : ")
    print(f'{name} 님 반갑습니다~')

    print('=================')       
    print('최고의 친구 월드컵')
    print('=================')
    time.sleep(1)
    a = input('보안서약서에 의거... 외부 발설하지 않으시겠습니까? [네 / 아니오] ')
    if a == '네' :
        before_final_list = before_final(player_list)
        final(before_final_list)
    else :
        print('그럼 쟌넨...')

    



