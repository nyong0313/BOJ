# 1753
# 다익스트라 : 시작점에서 다른 모든 정점으로의 [최단 경로**]를 구하는 알고리즘 -> 우선순위 큐
# 우선순위 큐 : (우선순위, 값)의 형태로 저장
# 위상정렬과 비슷한것 같아서 비슷하게 짜봤더니 시간초과네
# 시간초과는 왜그런지 모르겠고, 사이클이 있을 수도 있어서 위상정렬은 적합하지 않음.
import sys
input = sys.stdin.readline
from queue import PriorityQueue

n, e = map(int, input().split())
k = int(input())
MAX_SIZE = n * 10
mylist = [[]for _ in range(n+1)]
visited = [False] * (n+1)
ans = [MAX_SIZE] * (n+1)
ans[k] = 0

for i in range(e):
    u, v, w = map(int, input().split())
    mylist[u].append((v, w))

myqueue = PriorityQueue()
myqueue.put((0, k))
while not myqueue.empty():
    node = myqueue.get()[1]
    # if visited[node]:
    #     continue
    visited[node] = True
    for i in mylist[node]:
        nextNode = i[0]
        nextDistance = i[1]
        if not visited[nextNode] and ans[nextNode] > ans[node] + nextDistance:
            ans[nextNode] = ans[node] + nextDistance
            myqueue.put((ans[nextNode], nextNode))

for i in range(1, n+1):
    if visited[i]:
        print(ans[i])
    else:
        print("INF")



# 위상정렬
# from collections import deque
# myqueue = deque()
# myqueue.append(k)
# while myqueue:
#     node = myqueue.popleft()
#     visited[node] = True
#     for i in mylist[node]:
#         nextNode = i[0]
#         nextDistance = i[1]
#         if not visited[nextNode]:
#             myqueue.append(nextNode)
#             ans[nextNode] = min(ans[nextNode], ans[node] + nextDistance)

# for i in range(1, n+1):
#     if ans[i] == MAX_SIZE:
#         print("INF")
#     else:
#         print(ans[i])