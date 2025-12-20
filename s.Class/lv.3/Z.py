# 1074
import sys
input = sys.stdin.readline

def sol(N,r,c):
    if N == 0:
        return 0
    
    else:
        return 2*(r%2)+(c%2) + 4*(sol(N-1, r//2, c//2))

N,r,c = map(int, input().split())
print(sol(N,r,c))