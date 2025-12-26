# 5525
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = list(input().strip())

p = ['I', 'O', 'I']
for _ in range(n-1):
    p.append('O')
    p.append('I')

ans = 0
cnt = 0
i = 0

while i < m-2:
    if s[i]=='I' and s[i+1]=='O' and s[i+2]=='I':
        cnt += 1
        if cnt >= n:
            ans += 1
        i += 2
    else:
        cnt = 0
        i += 1

print(ans)