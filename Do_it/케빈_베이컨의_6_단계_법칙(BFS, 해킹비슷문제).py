#1389
#1325 효율적인 해킹 비슷한 문제로 풀었음.
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
mylist = [[]for _ in range(n+1)]
myqueue = deque()

for i in range(m):
    a, b = map(int, input().split())
    mylist[a].append(b)
    mylist[b].append(a)

def BFS(v):
    visited = [False] * (n+1)
    visited[v] = True
    myqueue.append((v, 1)) # node, count

    while myqueue:
        node = myqueue.popleft()
        for i in mylist[node[0]]:
            if not visited[i]:
                visited[i] = True
                kevinBacon[i] = node[1]
                myqueue.append((i, node[1] + 1))

ans = [0] * (n+1)
for i in range(1, n+1):
    kevinBacon = [0] * (n+1)
    BFS(i)
    ans[i] = sum(kevinBacon)

minAns = ans[1]
for i in range(1, n+1):
    if ans[i] < minAns:
        minAns = ans[i]

for i in range(1, n+1):
    if minAns == ans[i]:
        print(i)
        break