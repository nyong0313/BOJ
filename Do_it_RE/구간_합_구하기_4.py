# ch03 - 3/11659
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0, 0)

s = [0 for _ in range(n+1)]
for i in range(1, n+1):
    s[i] = s[i-1] + a[i]

for _ in range(m):
    i, j = map(int, input().split())
    print(s[j] - s[i-1])