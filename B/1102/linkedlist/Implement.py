import sys;sys.stdin=open('input.txt')
NODE_MAX = 5000

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None, tail=None, nodeCnt=0):
        self.nodeArr = [None for _ in range(NODE_MAX)]
        self.head = head
        self.tail = tail
        self.nodeCnt = nodeCnt

    def getNewNode(self, data):
        self.nodeArr[self.nodeCnt] = Node(data)
        self.nodeCnt += 1
        return self.nodeArr[self.nodeCnt - 1]

    def insert(self, idx, nums):
        st = 0
        if idx == 0:
            if self.head != None:
                newNode = self.getNewNode(nums[0])
                newNode.next = self.head
                self.head = newNode
            else:
                self.head = self.getNewNode(nums[0])

            idx = 1
            st = 1

        cur = self.head
        for i in range(1, idx):
            cur = cur.next

        for i in range(st, len(nums)):
            newNode = self.getNewNode(nums[i])
            newNode.next = cur.next
            cur.next = newNode
            cur = newNode

        if cur.next == None:
            self.tail = cur

    def remove(self, idx, cnt):
        cur = self.head
        if idx == 0:
            for i in range(cnt):
                cur = cur.next

            self.head = cur
            return

        for i in range(1, idx):
            cur = cur.next
        anchor = cur

        for i in range(cnt):
            cur = cur.next
        anchor.next = cur.next

        if anchor.next == None:
            self.tail = anchor

    def add(self, data):
        cur = self.tail
        newNode = self.getNewNode(data)
        cur.next = newNode
        self.tail = newNode

    def print(self):
        cnt = 10
        cur = self.head
        for i in range(cnt):
            print(cur.data, end=' ')
            cur = cur.next

T = 10

for t in range(1, T + 1):
    lst = LinkedList()

    print(f'#{t} ', end='')

    N = int(input())
    initArr = list(map(int, input().split()))
    lst.insert(0, initArr)

    M = int(input())
    input_line = input().split()
    idx = 0

    for i in range(M):
        cmd = input_line[idx]
        idx += 1

        if cmd == 'I':
            x = int(input_line[idx])
            idx += 1
            y = int(input_line[idx])
            idx += 1

            temp = []
            for j in range(y):
                temp.append(int(input_line[idx]))
                idx += 1
            lst.insert(x, temp)
        elif cmd == 'D':
            x = int(input_line[idx])
            idx += 1
            y = int(input_line[idx])
            idx += 1

            lst.remove(x, y)
        elif cmd == 'A':
            y = int(input_line[idx])
            idx += 1
            for j in range(y):
                lst.add(int(input_line[idx]))
                idx += 1

    lst.print()
    print()