#정렬 전 index - 정렬 후 index = 숫자가 왼쪽으로 이동한 거리
#숫자가 왼쪽으로 이동할떼는 for문 1번당 1번밖에 이동 못하므로
#해당 숫자가 제일 큰 숫자가 for문이 다 끝나서 정렬된 지점이라는 뜻.
import sys
input = sys.stdin.readline
n = int(input())
mylist = [] 

for i in range(n):
    mylist.append((i, int(input()))) # (정렬 후 인덱스, 정렬 전 값)

sortedlist = sorted(mylist, key=lambda x: x[1]) # 1번 키(정렬 전 인덱스, 정렬 후 값)

max = 0
for i in range(n):
    if max < sortedlist[i][0] - i:
        max = sortedlist[i][0] - i

# 정렬이 된 후 마지막 검사를 하는 단계 + 1 필요. / 예시 -> gpt
print(max+1)