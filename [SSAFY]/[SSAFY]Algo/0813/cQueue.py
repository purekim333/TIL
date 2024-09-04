Q_SIZE = 4
cQ = [0]*Q_SIZE
front = rear = 0

rear = (rear+1)%Q_SIZE
cQ[rear] = 1

rear = (rear+1)%Q_SIZE
cQ[rear] = 2

rear = (rear+1)%Q_SIZE
cQ[rear] = 3

front = (front+1)%Q_SIZE
print(cQ[front])

front = (front+1)%Q_SIZE
print(cQ[front])

rear = (rear+1)%Q_SIZE
cQ[rear] = 10

rear = (rear+1)%Q_SIZE
cQ[rear] = 20