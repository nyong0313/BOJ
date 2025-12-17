import sys
input = sys.stdin.readline

# 큰 숫자가 x
def gcd(x, y):
    r = x % y
    if r == 0:
        return y
    else:
        return gcd(y, r)

n = int(input())
for _ in range(n):
    y, x = map(int, input().split())
    # 최소 공배수 = 두 수 곱하기 나누기 최소 공약수 **
    print(x * y // gcd(x, y))