# 1916
# 최소비용 -> 최단경로 -> 다익스트라
import sys
input = sys.stdin.readline
from queue import PriorityQueue
n = int(input())
m = int(input())
mylist = [[]for _ in range(n+1)]
ans = [sys.maxsize] * (n+1)
visited = [False] * (n+1)

for i in range(m):
    u, v, w = map(int, input().split())
    mylist[u].append((v, w))

startNode, endNode = map(int, input().split())
ans[startNode] = 0

myqueue = PriorityQueue()
myqueue.put((ans[startNode], startNode))
while not myqueue.empty():
    node = myqueue.get()[1]
    if visited[node]: # 이거 없어도 되지만 효율성 문제로 추가해야함.
        continue
    visited[node] = True
    for i in mylist[node]:
        nextNode = i[0]
        nextDistance = i[1]
        if not visited[nextNode] and ans[nextNode] > ans[node] + nextDistance:
            ans[nextNode] = ans[node] + nextDistance
            # visited[nextNode] = True
            myqueue.put((ans[nextNode], nextNode))

print(ans[endNode])