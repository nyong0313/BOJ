import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
visited = [False] * (n+1)
a = [[] for _ in range(n+1)]
componentCount = 0

# for i in range(1, n+1):
#     a[i] = i

for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

def dfs(u):
    for i in a[u]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

for i in range(1, n+1):
    if not visited[i]:
        visited[i] = True
        dfs(i)
        componentCount += 1

print(componentCount)