import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def Count(len):
   cnt = 1
   ep = a[0]  # end point 를 첫번째 마구간에
   for i in range(1,n) :
      if a[i]-ep >= len : # 마지막 말과의 거리 len 보다 크면 -> 말 배치 가능
         cnt += 1
         ep = a[i]
   return cnt

#n = int(input())  # N 명
n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

a = [int(input()) for _ in range(n)]
print(a)
a.sort()

lt = 1
rt = a[n-1]   # max(a)
print(lt, rt)
res = 0
while lt <= rt :
   mid = (lt+rt)//2
   if Count(mid)>=k :
      res = mid     # 답이 됬음
      lt = mid +1   # 인접한 최대를 찾아야 함.
   else :
      rt = mid -1
print(res)

'''
1 2  4    8 9

lt      rt
1       9
    5 (보다 크거나 같아야) -> 2마리 밖에 배치 못함

1       4 로 바꿈
    2 -> 3마리 배치 가능

3       4 로 바꿈
    3 -> 3마리 가능
	
'''