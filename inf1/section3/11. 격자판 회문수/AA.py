import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, m = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

# 문제에서 7 X 7 가정
n = 7
a = [list(map(int, input().split())) for _ in range(n)]

def check_same(x) :
    rtn_value = True
    for i in range(len(x)//2):  # 몫으로 나눈 갯수
        if x[i] != x[(i+1)*(-1)] :
            rtn_value =  False
            break
    return rtn_value

tot = 0
# 행우선
for i in range(n):
    c_s = 0
    c_e = 5  # 5자리 회문수
    for j in range (3) :
        tmp_list = []
        for k in range(c_s, c_e):
            #print(k , end=' ')
            tmp_list.append(a[i][k])
        #print(tmp_list)
        #print(check_same(tmp_list))
        if check_same(tmp_list) :
            tot += 1
        c_s += 1
        c_e += 1
        #print()

# 열우선
for i in range(n):
    c_s = 0
    c_e = 5  # 5자리 회문수
    for j in range (3) :
        tmp_list = []
        for k in range(c_s, c_e):
            tmp_list.append(a[k][i])
        #print(tmp_list)
        #print(check_same(tmp_list))
        if check_same(tmp_list) :
            tot += 1
        c_s += 1
        c_e += 1
        #print()

print(tot)