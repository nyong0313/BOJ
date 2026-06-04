K, N = map(int, input().split())

ans = []

def dfs():
    if len(ans) >= N:
        print(*ans)
        return

    for i in range(1, K+1):
        ans.append(i)
        dfs()
        ans.pop()

dfs()