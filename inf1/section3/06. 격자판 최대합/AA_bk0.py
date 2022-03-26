import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

n = int(input())  # N 명
#n, m = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

#최대합
max = 0
two = []
for i in range(n):
    a = list(map(int, input().split()))
    #print(a)
    two.append(a)
    #print(sum(a))
    tmp = sum(a)
    if max < tmp :
        max = tmp

#print(two)

#열 계산
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += two[j][i]
    if max < tmp :
        max = tmp

#print(max)

# X 계산
tmp1 = 0
tmp2 = 0
for i in range(n):
    for j in range(n):
        if i == j :
            tmp1 += two[i][j]
        if j == j-i :
            tmp2 += two[i][j]

if max < tmp1 :
    max = tmp1
if max < tmp2 :
    max = tmp2
print(max)