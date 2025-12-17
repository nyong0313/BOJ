# 1033
# 전체 최소 공배수 찾은 다음 각 비율마다 나누기.
# -> 그래프로 구현하여 DFS로 하나씩 찾아서 나누기.
import sys
input = sys.stdin.readline

def gcd(x, y):
    r = x % y
    if r == 0:
        return y
    else:
        return gcd(y, r)
    
def dfs(v):
    visited[v] = True
    for i in arr[v]:
        next = i[0]
        if not visited[next]:
            ans[next] = ans[v] * i[2] // i[1]
            dfs(next)

n = int(input())
visited = [False] * n
arr = [[] for _ in range(n)]
ans = [0] * n

lcm = 1
for i in range(n-1):
    a, b, p ,q = map(int, input().split())
    if p > q:
        lcm *= p * q // gcd(p, q)
    else:
        lcm *= q * p // gcd(q, p)
    arr[a].append((b, p , q))
    arr[b].append((a, q , p))

ans[0] = lcm
dfs(0)

mgcd = ans[0]
for i in ans:
    if mgcd > i:
        mgcd = gcd(mgcd, i)
    else:
        mgcd = gcd(i, mgcd)

for i in ans:
    print(i // mgcd, end=" ")