# ch05 - 23/11724
# 방향없는 그래프, 그래프 묶음(?) 개수 -> DFS or BFS
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n, m = map(int, input().split())
visited = [False]*(n+1)
myList = [[]for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    myList[u].append(v)
    myList[v].append(u)

def DFS(v):
    visited[v] = True
    for i in myList[v]:
        if not visited[i]:
            DFS(i)

ans = 0
for i in range(1, n+1):
    if not visited[i]:
        ans += 1
        DFS(i)

print(ans)