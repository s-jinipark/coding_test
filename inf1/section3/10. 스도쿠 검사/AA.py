import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, m = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

# 문제에서 9 X 9 가정
n = 9
a = [list(map(int, input().split())) for _ in range(n)]

#print(a)
ok = True
#각 행 조사
for i in range(n):
    #rint(a[i])
    tmp = set(a[i])  # order 가 됨
    #print(len(tmp))
    if len(tmp) != 9 :
        ok = False
        break

# 각 열 조사
for i in range(n):
    tmp_list = []
    for j in range(n):
        tmp_list.append(a[j][i])
    tmp = set(tmp_list)
    if len(tmp) != 9 :
        ok = False
        break

# 3 * 3 씩 조사
size = 3
r_sno = 0
r_eno = size
c_sno = 0
c_eno = size

for cnt in range(size):
    tmp_list = []
    for i in range(r_sno, r_eno):
        for j in range(c_sno, c_eno):
            tmp_list.append(a[i][j])
    tmp = set(tmp_list)
    if len(tmp) != 9 :
        ok = False
        break
    r_sno += size
    r_eno += size
    c_sno += size
    c_eno += size

#print(ok)
if ok :
    print('YES')
else :
    print('NO')