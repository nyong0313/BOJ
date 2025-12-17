import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = []

def dfs(v):
    if len(ans) == m:
        print(*ans)
        return
    
    prev = 0
    for i in range(v, n):
        if prev != a[i]:
            ans.append(a[i])
            prev = a[i]
            dfs(i)
            ans.pop()

dfs(0)