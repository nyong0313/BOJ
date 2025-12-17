import sys
sys.setrecursionlimit(1000000)
v = int(input())
e = int(input())
myList = [[]for _ in range(v+1)]
visited = [False]*(v+1)

for i in range(e):
    a, b = map(int, input().split())
    myList[a].append(b)
    myList[b].append(a)

def DFS(v):
    global ans
    visited[v] = True
    for i in myList[v]:
        if not visited[i]:
            ans += 1
            DFS(i)

ans = 0
DFS(1)
print(ans)