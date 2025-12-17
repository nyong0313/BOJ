import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
a, b, c = map(int, input().split())

def fpow(b):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        temp = fpow(b // 2)
        return (temp * temp) % c
    else:
        temp = fpow((b-1) // 2)
        return (temp * temp * a) % c

print(fpow(b))