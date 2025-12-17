import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = []

def dfs(v):
    if len(s) == m:
        print(*s)
    else:
        for i in range(n):
            if a[i] not in s:
                s.append(a[i])
                dfs(i)
                s.pop()

dfs(0)

# def backtracking(depth):
#     if depth == m:
#         print(*s)
#         return

#     for i in range(n):
#         if a[i] in s:
#             continue
#         s.append(a[i])
#         backtracking(depth + 1)
#         s.pop()