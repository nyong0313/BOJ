#1717
# 합집합 -> 노드 연결. union
# 두 원소가 같은 집합에 포함돼 있다 = 대표노드가 동일하다. find
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def Find(a):
    
    # global mylist 리스트 선언 시, 디폴트 전역 변수임.
    index = a
    value = mylist[a]
    if index == value:
        return value
    else:
        value = Find(value)
        mylist[a] = value
        # 재귀적으로 봤을때, if절에 해당될때는 반환값이 업데이트를 해주고
        # 최종적으로 업데이트된 value값. 아래 있는 value를 반환해줘야한다.
        # 만약 리턴 없을시, 업데이트만 해주고 최종적인 반환값은 없음.
        return value
# if mylist[a] == a:
#     return a
# else:
#     mylist[a] = Find(mylist[a])
#     return mylist[a]
    

def Union(a, b):
    a_parant = Find(a)
    b_parant = Find(b)
    mylist[b_parant] = a_parant

n, m = map(int, input().split())
mylist = [i for i in range(n+1)]

for i in range(m):
    k, a, b = map(int, input().split())
    if k == 0:
        Union(a, b)
    else:
        if Find(a) == Find(b):
            print("YES")
        else:
            print("NO")