# 1504
import sys, heapq
input = sys.stdin.readline
n, e = map(int, input().split())
myList = [[]for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    myList[a].append((b, c))
    myList[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(i, j):
    ans = [sys.maxsize]*(n+1)
    ans[i] = 0
    hq = [(0, i)]

    while hq:
        nowD, nowNode = heapq.heappop(hq)

        if nowD > ans[nowNode]:
            continue

        for nextNode, nextD in myList[nowNode]:
            d = nowD + nextD
            if ans[nextNode] > d:
                ans[nextNode] = d
                heapq.heappush(hq, (d, nextNode))
    
    if ans[j] == sys.maxsize:
        return -1
    return ans[j]

t = [1, v1, v2, n]
result1 = 0

for i in range(3):
    temp = dijkstra(t[i], t[i+1])
    if temp == -1:
        result1 = -1
        break
    result1 += temp

t2 = [1, v2, v1, n]
result2 = 0

for i in range(3):
    temp = dijkstra(t2[i], t2[i+1])
    if temp == -1:
        result2 = -1
        break
    result2 += temp

print(min(result1, result2))