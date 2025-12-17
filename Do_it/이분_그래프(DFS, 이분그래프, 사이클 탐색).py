# 1707
# 사이클 없으면 무조건 이분그래프.
# -> 방문하지 않은 노드는 다른 집합을 주고.
# -> 방문했던 노드일때, 해당 노드와 집합을 비교함.
# 근데 방향성이 있는 그래프인지 아닌지 어떻게 구분할까
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def DFS(v):
    global ans
    visited[v] = True
    if graphSet[v] == "A":
        nextSet = "B"
    else:
        nextSet = "A"
    for i in mylist[v]:
        if not visited[i]:
            visited[i] = True
            graphSet[i] = nextSet
            DFS(i)
        elif graphSet[v] == graphSet[i]:
            ans = False

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    mylist = [[]for _ in range(v+1)]
    visited = [False] * (v+1)
    for i in range(e):
        a, b = map(int, input().split())
        mylist[a].append(b)
        mylist[b].append(a)
    
    ans = True
    graphSet = [0] * (v+1)
    for i in range(1, v):
        if graphSet[i] == 0:
            graphSet[i] = "A"
        if ans:
            DFS(i)
        else:
            break
    
    if ans:
        print("YES")
    else:
        print("NO")