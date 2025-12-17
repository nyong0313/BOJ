import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
a, b = map(int, input().split())
ans = []

def DFS(n, cnt):
    if n == b:
        ans.append(cnt)
        return
    elif n > b:
        return
    
    DFS(n*2, cnt+1)
    DFS(n*10+1, cnt+1)

DFS(a, 1)

if len(ans) == 0:
    print(-1)
else:
    print(min(ans))