# ch08 - 64/1197
import sys, heapq
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
v, e = map(int, input().split())
visited = [False]*(v+1)
edge = []

for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(edge, (c, a, b))

parent = [i for i in range(v+1)]
def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a != parent_b:
        parent[parent_b] = parent_a

ans = 0
cnt = 0
while cnt < v-1:
    w, s, e = heapq.heappop(edge)
    if find(s) != find(e):
        union(s, e)
        ans += w
        cnt += 1

print(ans)