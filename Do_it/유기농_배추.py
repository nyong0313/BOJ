t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    a = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]

    for i in range(k):
        x, y = map(int, input().split())
        a[x][y] = 1

    def dfs(i, j):
        visited[i][j] = True
        for l in range(4):
            x = i + dx[l]
            y = j + dy[l]
            if a[x][y] == 1 and not visited[x][y]:
                dfs(x, y)

    # 우, 하, 좌, 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    count = 0
    for i in range(m):
        for j in range(n):
            if a[i][j] == 1 and not visited[i][j]:
                count += 1
                dfs(i, j)
    
    print(count)