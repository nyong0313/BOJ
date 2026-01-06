# 1967
# Key 1: 아무 노드에서 가장 멀리 있는 노드를 찾고 그 노드에서 가장 멀리 있는 점 찾으면 최장 거리
# Key 2: 트리는 경로가 유일하니까, 한 번 방문할 때 계산한 dist가 곧 그 노드까지의 거리
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())
ml = [[]for _ in range(n+1)]
for _ in range(n-1):
    s, e, w = map(int, input().split())
    ml[s].append((e, w))
    ml[e].append((s, w))

def dfs(start):
    for node, w in ml[start]:
        if dist[node] == -1:
            dist[node] = dist[start] + w
            dfs(node)

dist = [-1]*(n+1)
dist[1] = 0
dfs(1)

v = 0
temp = 0
for i in range(1, n+1):
    if temp < dist[i]:
        temp = dist[i]
        v = i

dist = [-1]*(n+1)
dist[v] = 0
dfs(v)
print(max(dist))