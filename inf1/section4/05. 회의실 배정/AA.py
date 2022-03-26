import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")


n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

#a = [int(input()) for _ in range(n)]

meeting = []
for i in range(n):
   s, e = map(int, input().split())
   meeting.append((s, e))   # 튜플 형태로 저장
#meeting.sort()
meeting.sort(key=lambda  x : (x[1], x[0]))
print(meeting)
et = 0   # end time  현재 회의의 끝나는 시간
cnt = 0
for s, e in meeting :
   if s >= et :
      et = e
      cnt += 1

print(cnt)

'''
가장 좋은 것을 선택한다.
대부분 그리디 문제는 정렬.
** 회의가 끝나는 시간을 기준으로 정렬
  => 빨리 끝나는 게 중요
  
2 3 => 끝나는 시간 기록
1 4 -> 안 맞아 버림
2 5 => 진행
4 6
..(이런 식)
'''

