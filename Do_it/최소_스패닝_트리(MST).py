# 백준 1197
# 최소 신장 트리(Minimum Spanning Tree) -> 엣지리스트, 유니온파인드
import sys, heapq
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def Find(a):
    if a == parant[a]:
        return a
    else:
        parant[a] = Find(parant[a])
        return parant[a]

def Union(a, b):
    parant[Find(b)] = Find(a)
    # a_parant = Find(a)
    # b_parant = Find(b)
    # if a_parant != b_parant:
    #     parant[b_parant] = a_parant

v, e = map(int, input().split())
edges = []
parant = [i for i in range(v+1)]

for i in range(e):
    start, end ,weight = map(int, input().split())
    heapq.heappush(edges, (weight, start, end))

sum = 0
count = 0
# 리스트 다 도는데 엣지(노드 수 - 1)개 연결되면 그만.
while edges:
    weight, start, end = heapq.heappop(edges)
    startParant = Find(start)
    endParant = Find(end)
    if startParant != endParant:
        Union(start, end)
        sum += weight
        count += 1
        if count == v-1:
            break

print(sum)