Data = [0, 4, 1, 3, 1, 2, 4, 1]
Counts = [0] * 5

N = len(Data)
Temp = [0] * N

for x in Data :
    Counts[x] += 1                           # Data의 원소 x를 가져와서 Counts[x]에 개수 기록

for i in range(1, 5):                        # COUNT[1] ~ COUNT[4] 까지 누적개수
    Counts[i] = Counts[i-1] + Counts[i]

for i in range(N-1, -1, -1) :
    Counts[Data[i]] -= 1                     # 누적 개수 1개 감소
    Temp[Counts[Data[i]]] = Data[i]

print(*Temp)