#10868
# 세그먼트 트리 : 이진 트리 
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

# 1. 2^k <= N를 만족하는 k(트리 높이) 구하기
treeHeight = 0
while 2 ** treeHeight < n:
    treeHeight += 1

# 2. 트리 사이즈 구하기
treeSize = 2 ** (treeHeight + 1)
leftIndex = 2 ** treeHeight
tree = [sys.maxsize] * treeSize

# 3. 리프노드 값 입력
for i in range(n):
    tree[leftIndex + i] = int(input())

# 4. 최소 트리
for i in range(treeSize-2, 1, -2):
    tree[i // 2] = min(tree[i], tree[i+1])

ans = []
for i in range(m):
    a, b = map(int, input().split())

    start = leftIndex + a - 1
    end = leftIndex + b - 1
    ans.clear()

    # 구간 최소 구하기 로직
    # 등호 계속 틀림 **
    while start <= end:
        if start % 2 == 1:
            ans.append(tree[start])
            start += 1
        if end % 2 == 0:
            ans.append(tree[end])
            end -= 1
        
        start = start // 2
        end = end // 2

    print(min(ans))