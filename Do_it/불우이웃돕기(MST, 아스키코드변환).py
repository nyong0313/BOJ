import sys, heapq
input = sys.stdin.readline
n = int(input())
myList = []
total = 0
for i in range(n):
    charList = list(input())
    for j in range(n):
        if charList[j] == '0':
            continue
        elif i == j: # 자기 자신에 대한 랜선 -> 엣지리스트엔 추가 안하고 랜선 총합에만 추가.
            if ord(charList[j]) > 96: # 소문자인 경우
                length = ord(charList[j]) - ord('a') + 1
                total += length
            else:
                length = ord(charList[j]) - ord('A') + 27
                total += length
        else:
            if ord(charList[j]) > 96: # 소문자인 경우
                length = ord(charList[j]) - ord('a') + 1
                heapq.heappush(myList, (length, i, j))
                total += length
            else:
                length = ord(charList[j]) - ord('A') + 27
                heapq.heappush(myList, (length, i, j))
                total += length

parant = [i for i in range(n)]

def Find(a):
    if a == parant[a]:
        return a
    else:
        parant[a] = Find(parant[a])
        return parant[a]
    
def Union(a, b):
    a_parant = Find(a)
    b_parant = Find(b)
    parant[b_parant] = a_parant

sumLength = 0
cnt = 0
while myList:
    weight, start, end = heapq.heappop(myList)
    if Find(start) != Find(end):
        Union(start, end)
        sumLength += weight
        cnt += 1

if cnt == n-1:
    print(total - sumLength)
else:
    print(-1)