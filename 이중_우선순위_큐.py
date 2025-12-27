# 7662
import sys, heapq
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    k = int(input())
    minq = []
    maxq = []
    index = 0
    length = 0
    visited = []

    for __ in range(k):
        cmd, n = input().split()
        n = int(n)

        if cmd == 'I':
            length += 1
            heapq.heappush(minq, (n, index))
            heapq.heappush(maxq, (-n, index))
            index += 1
            visited.append(False)
        elif cmd == 'D':
            if length == 0:
                continue
            if n == 1:
                while True:
                    temp = heapq.heappop(maxq)
                    if not visited[temp[1]]:    
                        break
            elif n == -1:
                while True:
                    temp = heapq.heappop(minq)
                    if not visited[temp[1]]:
                        break
            length -= 1
            visited[temp[1]] = True
    
    if length == 0:
        print("EMPTY")
    else:
        while True:
            temp = heapq.heappop(maxq)
            if not visited[temp[1]]:    
                print(-temp[0], end=" ")
                break
        while True:
            temp = heapq.heappop(minq)
            if not visited[temp[1]]:
                print(temp[0])
                break