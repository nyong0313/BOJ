#1325 DFS로 할라했는데 BFS가 맞는듯. DFS가 맞는듯.
# 아 문제 잘못 이해함. 방향성이 있었음.
# 그냥 풀면 시간초과,,, 왜지,,
# 신뢰도 받으면 신뢰도를 증가시켜서 신뢰도 높은거 출력하자. -> BFS -> deque = FIFO
# 근데 이 문제에서 DFS하면 어떻게 될까,, DFS, BFS 시간복잡도는?
# pypy3으로 제출해야함.
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
mylist = [[]for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    mylist[a].append(b)

myqueue = deque()
def BFS(v):
    visited[v] = True
    myqueue.append(v)
    while myqueue:
        node = myqueue.popleft()
        for i in mylist[node]:
            if not visited[i]:
                ans[i] += 1
                visited[i] = True
                myqueue.append(i)

ans = [0]*(n+1)
for i in range(1, n+1):
    visited = [False]*(n+1)
    BFS(i)

maxAns = max(ans)
for i in range(1, n+1):
    if ans[i] == maxAns:
        print(i, end=" ")



# def DFS(v, count):
#     global maxCount

#     if maxCount < count:
#         maxCount = count
#     visited[v] = True
#     for i in mylist[v]:
#         if not visited[i]:
#             DFS(i, count + 1)