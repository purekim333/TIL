import sys; sys.stdin = open('input.txt')

'''
주어진 트리를 in-order 형식으로 순회해 각 노드를 읽으면 특정 단어를 알 수 있다.
 


 
위 트리를 in-order 형식으로 순회할 경우 SOFTWARE 라는 단어를 읽을 수 있다.
주어진 트리를 in-order 형식으로 순회했을때 나오는 단어를 출력하라.

[제약 사항]

트리는 완전 이진 트리 형식으로 주어지며, 노드당 하나의 문자만 저장할 수 있다.

노드는 아래 그림과 같은 순서로 주어진다.
 


[입력]

총 10개의 테스트 케이스가 주어진다. (총 테스트 케이스의 개수는 입력으로 주어지지 않는다)

각 테스트 케이스의 첫 줄에는 트리가 갖는 정점의 총 수 N(1≤N≤100)이 주어진다. 그 다음 N줄에 걸쳐 각각의 정점 정보가 주어진다.

정점 정보는 해당 정점의 문자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호 순서로 주어진다.

정점 번호는 1부터 N까지의 정수로 구분된다. 정점 번호를 매기는 규칙은 위 와 같으며, 루트 정점의 번호는 항상 1이다.

위의 예시에서,  알파벳 ‘F’가 2번 정점에 해당하고 두 자식이 각각 알파벳 ‘O’인 4번 정점과 알파벳 ‘T’인 5번 정점이므로 “2 F 4 5”로 주어진다.
알파벳 S는 8번 정점에 해당하므로 “8 S” 로 주어진다.


[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
'''
'''입력
8                // 첫 번째 케이스의 N
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
........
'''
def pre_order(T):
    if T:
        pre_order(left[T])
        print(word[T], end = '')
        pre_order(right[T])


for tc in range(1, 11) :
    V = int(input())
    E = V - 1

    par = [0] * (V+1)
    left = [0] * (V+1)
    right = [0] * (V+1)
    word = [0] * (V+1)

    for _ in range(V) :
        info = list(input().split())
        p = int(info[0])
        string = info[1]

        if len(info) > 3 :
            l = int(info[2])
            r = int(info[3])
            
        elif len(info) > 2:
            l = int(info[2])
            r = 0
            
        else :
            l = 0
            r = 0

        left[p] = l
        right[p] = r
        par[l] = p
        par[r] = p
        word[p] = string

    print(f'#{tc}', end=' ')
    pre_order(1)
    print()
