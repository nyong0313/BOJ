from collections import deque

# A, B, C 용량
bottle = list(map(int, input().split()))
myqueue = deque()

# 전체 용량은 정해져있기 때문에 A, B의 양만 체크.
visited = [[False for _ in range(201)]for _ in range(201)]

# Answer은 A가 0일때, C의 양.
ans = [False] * 201

# 6가지: A->B, A->C, B->A, B->C, C->A, C->B
# 위 여섯가지 경우의 수 계속 반복.
# 물의 양이 같은 경우 Stop.
sender = [0, 0, 1, 1, 2, 2]
receiver = [1, 2, 0, 2, 0, 1]

# BFS
visited[0][0] = True
myqueue.append((0, 0))
ans[bottle[2]] = True
# now는 현재 A, B, C 물의 양.
now = [0] * 3
while myqueue:
    node = myqueue.popleft()
    x = node[0]
    y = node[1]
    z = bottle[2] - (node[0] + node[1])
    for i in range(6):
        now[0] = x
        now[1] = y
        now[2] = z
        now[receiver[i]] += now[sender[i]]
        if now[receiver[i]] > bottle[receiver[i]]:
            now[sender[i]] = now[receiver[i]] - bottle[receiver[i]]
            now[receiver[i]] = bottle[receiver[i]]
        else:
            now[sender[i]] = 0
        
        if not visited[now[0]][now[1]]:
            visited[now[0]][now[1]] = True
            myqueue.append((now[0], now[1]))
            if now[0] == 0:
                ans[now[2]] = True

for i in range(201):
    if ans[i]:
        print(i, end=" ")