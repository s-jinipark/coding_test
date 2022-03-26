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
dic1 = []
dic2 = []
for i in range(n):
    dic1.append(input() )
#print(dic1)
# 다음은 N-1 이라는 조건이 있으니까....
for i in range(n-1):
    dic2.append(input() )

for j in dic2 :
    dic1.remove( j)
print(dic1.pop())

'''
미리 읽은 걸 두고
새로 읽은 것 비교 
=> 집합으로 만들어 빼면 될 듯

'''



