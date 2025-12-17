# ch08 - 50/1717
n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(p):
    if parent[p] == p:
        return p
    else:
        parent[p] = find(parent[p])
        return parent[p]

def union(p, q):
    parent_p = find(p)
    parent_q = find(q)
    if parent_p != parent_q:
        parent[parent_q] = parent_p

for _ in range(m):
    k, a, b = map(int, input().split())
    if k == 0:
        union(a, b)
    elif k == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")