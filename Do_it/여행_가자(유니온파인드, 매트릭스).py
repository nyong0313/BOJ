# 1976
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def Find(a):
    if mylist[a] == a:
        return a
    else:
        mylist[a] = Find(mylist[a])
        return mylist[a]
    
def Union(a, b):
    a_parant = Find(a)
    b_parant = Find(b)
    mylist[b_parant] = a_parant

n = int(input())
m = int(input())
# 문제와 달리 인덱스 0부터 시작
mylist = [i for i in range(n)]
for i in range(n):
    k = list(map(int, input().split()))
    for j in range(n):
        if k[j] == 1:
            Union(i, j)

route = list(map(int, input().split()))
route_parant = []
for i in route:
# 문제와 달리 인덱스 0부터 시작
    route_parant.append(Find(i-1))

check = route_parant[0]
isConnect = True
for i in route_parant:
    if check != i:
        isConnect = False
        break

if isConnect:
    print("YES")
else:
    print("NO")