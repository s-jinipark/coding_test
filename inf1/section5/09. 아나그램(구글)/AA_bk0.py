import sys
from collections import deque

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))
s1 = input()
s2 = input()
dic1 = {}

for c in s1:
    #print(c)
    if c in dic1 :
        dic1[c] = dic1.get(c) +1
    else :
        dic1[c] =1
#print(dic1)

for c in s2:
    #print(c)
    if c in dic1 :
        dic1[c] = dic1.get(c) - 1
#print(dic1)

#print(dic1.keys())
res = 'YES'
for x in dic1.keys() :
    #print(dic1.get(x))
    if dic1.get(x) >0 :
        res = 'NO'
print(res)