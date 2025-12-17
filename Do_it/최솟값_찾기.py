import sys
input = sys.stdin.readline
from collections import deque

n, l = map(int, input().split())
a = list(map(int, input().split()))

mydeque = deque()
d = [0] * n

for i in range(n):
    #mydeque
    while len(mydeque) != 0 and mydeque[-1][0] > a[i]:
        mydeque.pop()

    mydeque.append((a[i], i))

    if mydeque[0][1] < i-l+1:
        mydeque.popleft()

    print(mydeque[0][0], end=" ")
