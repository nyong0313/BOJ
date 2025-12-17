# ch05 - 26/1260
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n, m, v = map(int, input().split())
myList = [[]for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    myList[i].append(j)
    myList[j].append(i)

for i in range(1, n+1):
    myList[i].sort()

def DFS(k):
    visited[k] = True
    print(k, end=" ")
    for i in myList[k]:
        if not visited[i]:
            DFS(i)

def BFS(k):
    visited[k] = True
    print(k, end=" ")
    myQueue = []
    myQueue.append(k)
    while myQueue:
        temp = myQueue.pop(0)
        for i in myList[temp]:
            if not visited[i]:
                print(i, end=" ")
                visited[i] = True
                myQueue.append(i)

visited = [False]*(n+1)
DFS(v)
print()
visited = [False]*(n+1)
BFS(v)