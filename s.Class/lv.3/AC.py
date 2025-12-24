# 5430
# R에서 실제 뒤집을 필요 없다. 단순 방향으로 생각.
# deque(x[1:-1].split(',')), print("[" + ",".join(dq) + "]")
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    p = list(input().strip())
    n = int(input())
    x = input().strip()

    if n == 0:
        dq = deque()
    else:
        dq = deque(x[1:-1].split(','))

    isError = False
    isReverse = False
    for i in range(len(p)):
        if p[i] == 'R':
            if isReverse:
                isReverse = False
            else:
                isReverse = True
        elif p[i] == 'D':
            if n < 1:
                isError = True
                break
            if isReverse:
                dq.pop()
            if not isReverse:
                dq.popleft()
            n -= 1

    if isError:
        print("error")
    else:
        if isReverse:
            dq.reverse()
        print("[" + ",".join(dq) + "]")
