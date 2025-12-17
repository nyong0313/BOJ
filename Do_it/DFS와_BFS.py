# 1260
import sys, queue
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m, start = map(int, input().split())
a = [[] for _ in range(n+1)]
myqueue = queue.Queue()
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

for i in range(1, n+1):
    a[i].sort()
    
def dfs(v):
    print(v, end=" ")
    visited[v] = True
    for i in a[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    myqueue.put(v)
    visited[v] = True

    while not myqueue.empty():
        node = myqueue.get()
        print(node, end=" ")

        for i in a[node]:
            if not visited[i]:
                visited[i] = True
                myqueue.put(i)

dfs(start)
print("")
visited = [False] * (n+1)
bfs(start)