# 11505
# 세그먼트 트리 - 구간 곱
# 0으로 바꿀때 주의
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

treeHeight = 0
while 2 ** treeHeight < n:
    treeHeight += 1

treeSize = 2 ** (treeHeight + 1)
leftIndex = 2 ** (treeHeight)

tree = [1] * treeSize
for i in range(n):
    tree[leftIndex + i] = int(input())

for i in range(treeSize - 2, 1, -2):
    tree[i//2] = (tree[i] * tree[i+1]) % 1000000007

for _ in range(m+k):
    a, b, c = map(int, input().split())
    ans = 1

    if a == 1:
        index = leftIndex + b - 1
        tree[index] = c
        while index > 1:
            index = index // 2
            tree[index] = tree[index * 2]  % 1000000007 * tree[index * 2 + 1] % 1000000007
        
        # if tree[index] == 0:
        #     tree[index] = c
        #     index = index // 2
        #     while index > 0:
        #         tree[index] = (tree[index * 2] * tree[index * 2 + 1]) % 1000000007
        #         index = index // 2
        
        # else:
        #     diff = tree[index]
        #     while index > 0:
        #         tree[index] = (tree[index] * c // diff) % 1000000007
        #         index = index // 2
    
    if a == 2:
        start = leftIndex + b - 1
        end = leftIndex + c - 1
        while start <= end:
            if start % 2 == 1:
                ans = (ans * tree[start]) % 1000000007
                start += 1
            if end % 2 == 0:
                ans = (ans * tree[end]) % 1000000007
                end -= 1
            start = start // 2
            end = end // 2
        print(ans)