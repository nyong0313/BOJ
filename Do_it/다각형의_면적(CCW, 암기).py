# 2166
def CCW(x1, y1, x2, y2): # 원점과 두 점 간의 CCW
    return (x1 * y2) - (x2 * y1)

import sys
input = sys.stdin.readline
n = int(input())
inputList = []

for _ in range(n):
    inputList.append(list(map(int, input().split())))

ans = 0
for i in range(1, n): 
    x1, y1 = inputList[i-1]
    x2, y2 = inputList[i]
    ans += CCW(x1, y1, x2, y2)
# 마지막 점과 첫 번째 점도 비교해야함.
ans += CCW(inputList[n-1][0], inputList[n-1][1], inputList[0][0], inputList[0][1])

ans = abs(ans/2)
print(round(ans, 1))