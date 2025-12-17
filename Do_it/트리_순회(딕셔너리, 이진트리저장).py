# 1991
# 딕셔너리 {} : 파이썬 자료구조
# 아이디어
# 이진트리를 배열로 저장하는 방법 -> 루트노드 배열을 만들고 값으로 왼쪽 오른쪽 저장. 
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())
tree = {}

for i in range(1, n+1):
    root, left, right = input().split()
    tree[root] = (left, right)  

def preorder(now):
    if now == '.':
        return
    
    print(now, end="")
    preorder(tree[now][0])
    preorder(tree[now][1])

def inorder(now):
    if now == '.':
        return
    inorder(tree[now][0])
    print(now, end="")
    inorder(tree[now][1])

def postorder(now):
    if now == '.':
        return
    postorder(tree[now][0])
    postorder(tree[now][1])
    print(now, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')