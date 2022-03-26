import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")


n = int(input())  # N
#n, k = map(int, input().split())
a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

#a = [int(input()) for _ in range(n)]

m = int(input())  # M

#창고 높이 조정은 가장 높은 곳에 상자를 가장 낮은 곳으로 이동하는 것을 말한다.

a.sort()
for i in range(m):
   #a.sort()
   #print(a)
   #a.append(a.pop()-1)
   a[0]+=1
   #print(a)
   #a.insert(0,a.pop(0)+1)
   a[n-1] -= 1
   #print(a)
   a.sort()
#print(a)
print(a[n-1] - a[0])