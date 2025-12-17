import sys
sys.setrecursionlimit(1000000)
t = int(input())
f = [(0, 0)] * 41

def fibonacci(n):
    if f[n] != (0, 0):
        return f[n]
    if n == 0:
        f[n] = (1, 0)
        return f[n]
    elif n == 1:
        f[n] = (0, 1)
        return f[n]
    else:
        a = fibonacci(n-1)
        b = fibonacci(n-2)
        f[n] = (a[0] + b[0], a[1] + b[1])
        return f[n]

for _ in range(t):
    n = int(input())
    ans = fibonacci(n)
    print(ans[0], ans[1])