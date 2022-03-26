import sys
from collections import deque

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))
n = int(input())  # N 명
p = dict()

for i in range(n):
    word = input()
    p[word] = 1  # 1 로 셋팅

for i in range(n-1):
    word = input()
    p[word] =0

for key, val in p.items() :  # key, value 동시
    if val == 1:
        print(key)
        break





