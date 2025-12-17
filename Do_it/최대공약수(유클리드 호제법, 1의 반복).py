import sys
input = sys.stdin.readline

# x가 큰수
def gcd(x, y):
    r = x % y
    if r == 0:
        return y
    else:
        return gcd(y, r)

a, b = map(int, input().split())

# 문제 그대로 풀면 안됨.
# 최대 공약수만큼 1이 반복된다는 점을 파악해야함.
for i in range(gcd(b, a)):
    print("1", end="")