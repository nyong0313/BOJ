# 15652
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
s = []

def backtrack(start):
    if len(s) == m:
        print(*s)
        return
    
    for i in range(start, n+1):
        s.append(i)
        backtrack(i)
        s.pop()

backtrack(1)