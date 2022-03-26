import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")


n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

#a = [int(input()) for _ in range(n)]
s = []
e = []

cnt = 0
for i in range(n) :
   t_s, t_e = map(int, input().split())
   s.append(t_s)
   e.append(t_e)
print(s)
print(e)
maxx = -1

for i in range(n):
   s_time = s[i]
   print(s_time)

print(maxx)