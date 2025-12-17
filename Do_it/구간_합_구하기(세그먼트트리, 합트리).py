# 2042
# 세그먼트 트리 부모는 자식 노드의 합.
# 여러 노드, 구간의 노드 합 구하는 로직 **
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

# 트리 높이
treeHeight = 0
while 2 ** treeHeight < n:
    treeHeight += 1

treeSize = 2 ** (treeHeight + 1)
tree = [0] * treeSize

# 리프노드 설정
for i in range(n):
    tree[2 ** treeHeight + i] = int(input())

# 합 트리
for i in range(treeSize-1, 2, -2):
    tree[i//2] = tree[i-1] + tree[i]

for i in range(m+k):
    a, b, c = map(int, input().split())

    if a == 1:
        index = 2 ** treeHeight + b - 1
        diff = c - tree[index]
        while index > 0:
            tree[index] += diff
            index = index // 2

    if a == 2:
        ans = 0
        start = 2 ** treeHeight + b - 1
        end = 2 ** treeHeight + c - 1
        
        
        while start <= end:
            if start % 2 == 1:
                ans += tree[start]
                start += 1
            if end % 2 == 0:
                ans += tree[end]
                end -= 1
            start = (start + 1) // 2
            end = (end - 1) // 2
        
        print(ans)
