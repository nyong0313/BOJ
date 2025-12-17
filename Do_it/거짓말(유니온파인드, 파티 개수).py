# 1043

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def Find(a):
    if a == people[a]:
        return a
    else:
        people[a] = Find(people[a])
        return people[a]
    
def Union(a, b):
    a_parant = Find(a)
    b_parant = Find(b)
    people[b_parant] = a_parant

n, m = map(int, input().split())
people = [i for i in range(n+1)]
testCase = []
x = list(map(int, input().split()))
x_len = x[0]
for i in range(m):
    testCase.append(list(map(int, input().split())))
    testCase_len = testCase[i][0]
    if testCase_len > 1:
        for j in range(2, testCase_len+1):
            Union(testCase[i][1], testCase[i][j])

count = 0
for i in range(m):
    isPossible = True # 과장 가능?
    for j in range(1, x_len+1): # people[x[j]] == xman (진실아는사람)
        if Find(testCase[i][1]) == Find(people[x[j]]):
            isPossible = False
            break
    if isPossible:
        count += 1

print(count)





# xman = [False] * (n+1)
# for i in range(k[0]):
#     xman[k[i+1]] = True
# truthParty = [False] * (m)
# for i in range(m):
#     testCase.append(list(map(int, input().split())))
#     for j in range(testCase[i][0]):
#         if xman[testCase[i][j+1]]:
#             truthParty[i] = True
#             break
    
#     if truthParty[i]:
#         for j in range(testCase[i][0]):
#             xman[testCase[i][j+1]] = True

# for i in range(m-1, -1, -1):
#     for j in range(testCase[i][0]):
#         if xman[testCase[i][j+1]]:
#             truthParty[i] = True
#             break
    
#     if truthParty[i]:
#         for j in range(testCase[i][0]):
#             xman[testCase[i][j+1]] = True

# count = 0
# for i in range(m):
#     if not truthParty[i]:
#         count += 1

# print(count)