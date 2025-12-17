# 11657
# 벨만포드 (<- 시간 C가 양수가 아닐때가 있다)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edges = []
distance = [sys.maxsize] * (n+1)

# 엣지 리스트 저장
for i in range(m):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

# 시작 노드 초기화
distance[1] = 0

# N-1번 엣지 사용 = N-1번 업데이트
for _ in range(n-1):
    # 모든 노드 체크
    for start, end, weight in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + weight:
            distance[end] = distance[start] + weight

# 음수 사이클 체크
mCycle = False
for start, end, weight in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + weight:
        mCycle = True

if mCycle:
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] == sys.maxsize:
            print(-1)
        else:
            print(distance[i])