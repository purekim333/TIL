# N = 10
# q = [0] * N
# front = -1
# rear = -1

# rear += 1
# q[rear] = 1
# rear += 1
# q[rear] = 2
# rear += 1
# q[rear] = 3

# front += 1
# print(q[front])
# front += 1
# print(q[front])
# front += 1
# print(q[front])

# q2 = []
# q2.append(10)
# q2.append(20)
# print(q2.pop(0))
# print(q2.pop(0))

#===============================

Q_SIZE = 4
Q = [0] * Q_SIZE

front = -1
rear = -1 #front는 빈 공간을 가리키고, rear는 가장 마지막에 들어온 데이터를 가리킴!

def my_enQueue(data) :
    global rear
    if isFull() :
        print('Queue is Full')
        return
    else :
        rear += 1
        Q[rear] = data

def my_deQueue() :
    global front
    if isEmpty() :
        print('Queue is Empty')
        return
    else :
        front += 1
        return Q[front]
    
def isEmpty():
    return front == rear

def isFull() :
    return rear == Q_SIZE - 1

for i in range(1,6) :
    my_enQueue(i)

print(Q)

while front != rear :
    print(my_deQueue())


#=============================================
# 원형 큐

Q_SIZE = 4
Q = [0] * Q_SIZE

front = rear = 0 #front는 빈 공간을 가리키고, rear는 가장 마지막에 들어온 데이터를 가리킴!

def my_enQueue(data) :
    global rear
    if isFull() :
        print('Queue is Full')
        return
    else :
        rear = (rear + 1) % Q_SIZE
        Q[rear] = data

def my_deQueue() :
    global front
    if isEmpty() :
        print('Queue is Empty')
        return
    else :
        front = (front + 1) % Q_SIZE
        return Q[front]
    
def isEmpty():
    return front == rear

def isFull() :
    return (rear + 1) % Q_SIZE == front

for i in range(1,6) :
    my_enQueue(i)

print(Q)

# while front != rear :
#     print(my_deQueue())