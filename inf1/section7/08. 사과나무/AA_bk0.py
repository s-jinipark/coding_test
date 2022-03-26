import sys
from collections import deque

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

n = int(input())  # n (홀수)
#n, m = map(int, input().split())  # 현수의 위치 (n)와 송아지의 위치 (m) 가 주어진다
farm = []
for _ in range(n):
    a = list(map(int, input().split()))
    farm.append(a)
#print(farm)

base = n//2
sum = 0

for i in range(n):
    if i < base :
        for j in range(base-i, base+i+1):
            #print(farm[i][j], end=' ')
            sum += farm[i][j]
        #print()
    elif i == base :
        for j in range(n):
            #print(farm[i][j], end=' ')
            sum += farm[i][j]
        #print()
    else :
        for j in range(i-base, n-i//2):
            #print(farm[i][j], end=' ')
            sum += farm[i][j]
        #print()
print(sum)
