from collections import deque

n = int(input())
mydeque = deque()

for i in range(n):
    mydeque.append(n-i)

while len(mydeque) > 1:
    mydeque.pop()
    mydeque.appendleft(mydeque.pop())

print(mydeque.pop())