import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

n = int(input())  # N 명
#n, m = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

#최대합
# max = 0
# two = []
# for i in range(n):
#     a = list(map(int, input().split()))
#     #print(a)
#     two.append(a)
#     #print(sum(a))
#     tmp = sum(a)
#     if max < tmp :
#         max = tmp

#한번에 적재
a = [list(map(int, input().split())) for _ in range(n)]

# #열 계산
# for i in range(n):
#     tmp = 0
#     for j in range(n):
#         tmp += two[j][i]
#     if max < tmp :
#         max = tmp

# 행, 열 따로 계산 했던 것 한번에 계산
max = -1
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > max :
        max = sum1
    if sum2 > max :
        max = sum2
print(max)

# X 계산
# tmp1 = 0
# tmp2 = 0
# for i in range(n):
#     for j in range(n):
#         if i == j :
#             tmp1 += two[i][j]
#         if j == j-i :
#             tmp2 += two[i][j]
#
# if max < tmp1 :
#     max = tmp1
# if max < tmp2 :
#     max = tmp2
# print(max)

# 대각선 계산도 이중루프에서 단일로
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]  # 아래에서 위로 올라가는 대각선
                         # 반대만 생각했다 .. ㅠ
if sum1 > max :
    max = sum1
if sum2 > max :
    max = sum2
print(max)