import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

# 2 회로 가정
n1 = int(input())
l1 = list(map(int, input().split()))
n2 = int(input())
l2 = list(map(int, input().split()))


l1.extend(l2)
l1.sort()
#print(l1)
for i in l1 :
    print(i, end=' ')