# ch08 - 56/1753
# readline 써야 시간초과 안걸림 ;;
# 다익스트라는 우선순위 큐 !!
# K번째 최단경로(58/1854번) 다시 풀기
import sys, heapq
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
myList = [[]for _ in range(v+1)]
visited = [False]*(v+1)
MAX_SIZE = v * 10
d = [MAX_SIZE]*(v+1)
d[k] = 0

for _ in range(e):
    a, b, w = map(int, input().split())
    myList[a].append((b, w))

# def dikstra(k):
myQueue = []
heapq.heappush(myQueue, (0, k))
while myQueue:
    node = heapq.heappop(myQueue)[1]
    visited[node] = True
    for i in myList[node]:
        if not visited[i[0]] and d[node] + i[1] < d[i[0]]:
            d[i[0]] = d[node] + i[1]
            heapq.heappush(myQueue, (d[i[0]], i[0]))

for i in range(1, v+1):
    if d[i] == MAX_SIZE:
        print("INF")
    else:
        print(d[i])