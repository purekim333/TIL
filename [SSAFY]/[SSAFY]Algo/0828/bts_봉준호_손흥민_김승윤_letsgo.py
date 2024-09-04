'''
7
3 5 1 2 7 4 -5
12
1 2 11 4 5 14 9 8 7 10 3 6
'''

# 노드 정의
class Node:
    def __init__(self, key) :
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

class BinarySearchTree :
    def __init__(self) : #객체 호출
        self.root = None

    def insert(self, key) : #삽입 연산
        if self.root is None : #root가 비어있으면 해당 노드의 키 값을 루트로 설정
            self.root = Node(key)
        else :
            self._insert(self.root, key)

    def _insert(self, node, key) :
        if key < node.key : #인자로 전달받은 키가 비교하는 노드의 키 보다 작다면
            if node.left is None :
                node.left = Node(key) #노드의 left 속성과 연결
                node.left.parent = node
            else :
                self._insert(node.left, key) # 꽉 차 있으면 왼쪽 서브트리로 이동

        else : #인자로 전달받은 키가 더 크다면
            if node.right is None : #노드 right이 비어있으면 채우기
                node.right = Node(key)
                node.right.parent = node
            else :
                self._insert(node.right, key) #꽉 차있으면 오른쪽 서브트리로 이동

    def delete(self, key) :#삭제 연산
        node_to_delete = self.search(key)
        if node_to_delete is not None :#부모와 자식을 넘겨줌 node, key
            self._delete(node_to_delete)
    
    # def _delete(self, node) :
    #     if node.parent.right == node : #부모와 right로 연결이 되어있나?
    #         # leaf 노드이면 연결을 삭제
    #         if key.left == None and key.right == None :
    #             node.right = None # 지우기
    #         #자식 노드이면
    #         elif key.left == None : #하나가 연결되어있고 그게 right 이면
    #             node.right = key.right
    #             self._delete(node, key.right)
    #         elif key.right == None : #하나가 연결되어있고 그게 left 이면
    #             node.right = key.left
    #             self._delete(node, key.left)
    #         else :  #두개가 연결되어있다면
    #             node.right = key.left
    #             self._delete(node, key.left)

    #     else : # 부모와 left로 연결이 되어 있나?
    #         # leaf 노드이면 연결을 삭제
    #         if key.left == None and key.right == None :
    #             node.left = None # 지우기
    #         #자식 노드이면
    #         elif key.left == None : #하나가 연결되어있고 그게 right 이면
    #             node.left = key.right
    #             self._delete(node, key.right)
    #         elif key.right == None : #하나가 연결되어있고 그게 left 이면
    #             node.left = key.left
    #             self._delete(node, key.left)
    #         else :  #두개가 연결되어있다면
    #             node.left = key.right
    #             self._delete(node, key.right)

    def _delete(self, node):
        # 리프 노드인 경우
        if node.left is None and node.right is None:
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = None
                elif node.parent.right == node:
                    node.parent.right = None
            else:
                self.root = None  # 트리의 루트 노드를 삭제하는 경우

        # 오른쪽 자식만 있는 경우
        elif node.left is None:
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
            else:
                self.root = node.right  # 루트 노드를 삭제하는 경우
            node.right.parent = node.parent

        # 왼쪽 자식만 있는 경우
        elif node.right is None:
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
            else:
                self.root = node.left  # 루트 노드를 삭제하는 경우
            node.left.parent = node.parent

        # # 두 자식이 모두 있는 경우
        # else:
        #     if node.parent :
        #         if node.parent.left == node:
        #             node.parent.left = node.right
        #             node.right.left = node.left
        #             self._delete(node.right)
        #         else:
        #             node.parent.right = node.left
        #             self._delete(node.left)

        # 두 자식이 모두 있는 경우
        else:
            # 오른쪽 자식을 현재 노드로 대체
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
            else:
                self.root = node.right  # 루트가 바뀌는 경우

            # 대체된 노드의 왼쪽에 원래 노드의 왼쪽 자식을 연결
            node.right.left = node.left
            if node.left:
                node.left.parent = node.right

            # 대체된 노드(오른쪽 자식)을 재귀적으로 삭제
            self._delete(node.right)


    def search(self, key) :
        return self._search(self.root, key)
    
    def _search(self, node, key) :
        if node is None or node.key == key :
            return node # 찾으려는 값에 도착하거나 값이 없으면 결과 반환
        if key < node.key : #입력값이 노드보다 작으면
            return self._search(node.left, key) #왼쪽 서브트리 가서 탐색
        else : # 입력값이 노드보다 크면
            return self._search(node.right, key) # 오른쪽 서브트리 가서 탐색
        
    def inorder_traversal(self) :
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node) : # 중위탐색
        if node : #노드가 존재하면
            self._inorder_traversal(node.left)
            print(node.key, end = ' ')
            self._inorder_traversal(node.right)

N = int(input())
arr = list(map(int, input().split()))

bst = BinarySearchTree()

for num in arr :
    bst.insert(num)

print('중위 순회 결과', end = ' ')
bst.inorder_traversal()

# 탐색 예제
key = 5
result = bst.search(key)
if result:
    print(f"\n키 {key} 찾음.")
else:
    print(f"\n키 {key} 못 찾음.")

key = 5
print(key, '삭제 시작')
bst.delete(key)

print('중위 순회 결과', end = ' ')
bst.inorder_traversal()
