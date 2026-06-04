n = int(input())

arr = []
ans = 0

def dfs():
    global ans

    length = len(arr)
    if length >= n:
        ans += 1
        return

    for i in range(1, 4+1):
        if length + i > n:
            continue

        for _ in range(i):
            arr.append(i)
        dfs()
        for _ in range(i):
            arr.pop()

dfs()
print(ans)