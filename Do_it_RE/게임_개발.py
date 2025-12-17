# ch08 - 54/1516
n = int(input())
myList = [[]for _ in range(n+1)]
time = [0]*(n+1)
d = [0]*(n+1) # 위상정렬 리스트

for i in range(1, n+1):
    inputList = list(map(int, input().split()))
    time[i] = inputList[0]

    for j in range(1, len(inputList)):
        if inputList[j] == -1:
            break
        myList[inputList[j]].append(i)
        d[i] += 1

myQueue = []
for i in range(1, n+1):
    if d[i] == 0:
        myQueue.append(i)
        break

ans = [0]*(n+1)
while myQueue:
    a = myQueue.pop(0)
    for i in myList[a]:
        ans[i] = max(ans[i], time[a] + ans[a]) # *** min 아니고 max임 !!!
        d[i] -= 1
        if d[i] == 0:
            myQueue.append(i)

for i in range(1, n+1):
    print(ans[i] + time[i])