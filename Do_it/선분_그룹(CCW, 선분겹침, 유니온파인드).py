# 2162
import sys
input = sys.stdin.readline
n = int(input())
inputList = []
parent = [-1]*n

def CCW(x1, y1, x2, y2, x3, y3):
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

def isOverlab(x1, y1, x2, y2, x3, y3, x4, y4):
    minXAB = min(x1, x2)
    maxXAB = max(x1, x2)
    minXCD = min(x3, x4)
    maxXCD = max(x3, x4)
    minYAB = min(y1, y2)
    maxYAB = max(y1, y2)
    minYCD = min(y3, y4)
    maxYCD = max(y3, y4)
    if minXAB <= maxXCD and minXCD <= maxXAB and minYAB <= maxYCD and minYCD <= maxYAB:
        return True
    return False

def isCross(x1, y1, x2, y2, x3, y3, x4, y4):
    abc = CCW(x1, y1, x2, y2, x3, y3)
    abd = CCW(x1, y1, x2, y2, x4, y4)
    cda = CCW(x3, y3, x4, y4, x1, y1)
    cdb = CCW(x3, y3, x4, y4, x2, y2)

    if abc * abd == 0 and cda * cdb == 0:
        if isOverlab(x1, y1, x2, y2, x3, y3, x4, y4):
            return True
        return False
    elif abc * abd <= 0 and cda * cdb <= 0:
        return True
    else:
        return False
    
def find(a):
    if parent[a] < 0:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    p = find(a)
    q = find(b)
    if p == q: # 이미 같은 그룹 (a, b의 루트 같을 경우) ***
        return
    parent[p] += parent[q]
    parent[q] = p # 같은 그룹이면 여기서 오류 발생

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(len(inputList)):
        if isCross(x1, y1, x2, y2, inputList[j][0], inputList[j][1], inputList[j][2], inputList[j][3]):
            union(i, j)
    inputList.append([x1, y1, x2, y2])

cnt = 0
ans = 0
for i in range(n):
    if parent[i] < 0:
        cnt += 1
        ans = max(ans, abs(parent[i]))

print(cnt)
print(ans)