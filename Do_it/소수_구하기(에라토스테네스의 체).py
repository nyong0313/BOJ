import math, sys
input = sys.stdin.readline

m, n = map(int, input().split())
# index를 실제 숫자로 취급.
a = [1] * (n+1)
a[0] = 0
a[1] = 0

for i in range(2, int(math.sqrt(n))+1):
    if a[i] == 0:
        continue

    else:
        for j in range(i + i, n + 1, i):
            a[j] = 0

for i in range(m, n+1):
    if a[i] != 0:
        print(i)