import sys

def bfs(v, count):
    if not cities[v]:
        if min_route[v] > count:
            min_route[v] = count

    else:
        min_route[v] = count

    for i in cities[v]:
        bfs(i, count + 1)

n, m, k, x = map(int, input().split())
cities = [[]for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    cities[a].append(b)

min_route = [m] * (n+1)
bfs(x, 0)
none_check = False
for i in range(1, n+1):
    if min_route[i] == k:
        none_check = True
        print(i)

if not none_check: print(-1)