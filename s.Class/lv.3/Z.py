# 1074
import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())
ans = 0

while n > 0:
    size = 2 ** n
    half = 2 ** (n-1)

    if 0 <= r < half and 0 <= c < half:
        k = 0
    elif 0<= r < half and half <= c < size:
        k = 1
        c -= half
    elif half <= r < size and 0 <= c < half:
        k = 2
        r -= half
    elif half <= r < size and half <= c < size:
        k = 3
        r -= half
        c -= half

    ans += k * 4**(n-1)
    n -= 1
    
print(ans)