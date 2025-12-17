# 13023
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
a = [[] for _ in range(n) ]
visited = [False] * n

for i in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

def dfs(v, count):
    if count == 5:
        print(1)
        exit()

    # 문제 특성 상, 방문 유무 매번 초기화 해줘야함 !!
    visited[v] = True
    for i in a[v]:
        if not visited[i]:
            dfs(i, count + 1)
    visited[v] = False

for i in range(n):
    # 실수 제발 !!!!!!
    # visited = [False] * n
    dfs(i, 1)

print(0)