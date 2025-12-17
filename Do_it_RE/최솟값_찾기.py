#ch03 - 10/11003
import sys
from collections import deque
input = sys.stdin.readline
n, l = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0, 0)
d = deque()

for i in range(1, n+1):
    while d and d[-1][0] > a[i]:
        d.pop()

    if d and d[0][1] < i-l+1:
        d.popleft()
    
    d.append((a[i], i))
    print(d[0][0], end=" ")