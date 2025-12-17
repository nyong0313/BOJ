import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna_list = input()
min_A, min_C, min_G, min_T = map(int, input().split())
output=0

# A, C, G, T
check_list = [0]*4

# 처음 0 ~ p-1의 비밀번호 체크리스트
for i in range(p):
    if dna_list[i] == "A":
        check_list[0] += 1

    elif dna_list[i] == "C":
        check_list[1] += 1

    elif dna_list[i] == "G":
        check_list[2] += 1

    elif dna_list[i] == "T":
        check_list[3] += 1

# 정답 조건 실수 ,,,
if min_A <= check_list[0] and min_C <= check_list[1] and min_G <= check_list[2] and min_T <= check_list[3]:
    output +=1
 
# P칸만큼 그대로 한칸씩 움직이면서 비밀번호 체크리스트 업데이트
for i in range(p, s):
    j = i - p
# 기존 칸 제거
    if dna_list[j] == "A":
        check_list[0] -= 1

    elif dna_list[j] == "C":
        check_list[1] -= 1

    elif dna_list[j] == "G":
        check_list[2] -= 1

    elif dna_list[j] == "T":
        check_list[3] -= 1
    
# 새로운 칸 추가
    if dna_list[i] == "A":
        check_list[0] += 1

    elif dna_list[i] == "C":
        check_list[1] += 1

    elif dna_list[i] == "G":
        check_list[2] += 1

    elif dna_list[i] == "T":
        check_list[3] += 1

    if min_A <= check_list[0] and min_C <= check_list[1] and min_G <= check_list[2] and min_T <= check_list[3]:
        output +=1
 
print(output)

# 시간초과
    # for j in range(i, i+p):
    #     if dna_list[j] == "A":
    #         A += 1
    #     elif dna_list[j] == "C":
    #         C += 1
    #     elif dna_list[j] == "G":
    #         G += 1
    #     elif dna_list[j] == "T":
    #         T += 1