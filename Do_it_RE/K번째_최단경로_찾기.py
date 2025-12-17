# ch08 - 58/1854
import sys, heapq
input = sys.stdin.readline
n, m, k = map(int, input().split())
myList = [[]for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    myList[a].append((b, c))

d = [[sys.maxsize for __ in range(k) ]for __ in range(n+1)]
d[1][0] = 0

myQueue = []
heapq.heappush(myQueue, (0, 1))
while myQueue:
    temp = heapq.heappop(myQueue)
    weight = temp[0]
    node = temp[1]

    for i in myList[node]:
        nextNode = i[0]
        nextWeight = i[1]
        nextD = weight + nextWeight

        if d[nextNode][-1] > nextD:
            d[nextNode][-1] = nextD
            d[nextNode].sort()
            heapq.heappush(myQueue, (nextD, nextNode))

for i in range(1, n+1):
    if d[i][-1] == sys.maxsize:
        print(-1)
    else:
        print(d[i][-1])