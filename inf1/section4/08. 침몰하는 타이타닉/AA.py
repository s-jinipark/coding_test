import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")


#n = int(input())  # N
n, k = map(int, input().split())
a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

#a = [int(input()) for _ in range(n)]

lt = 0
rt = n-1
a.sort()
#sprint(a)
cnt = 0
while a :  # list 값이 없을때 까지
    if len(a) == 1 :  # a 의 값이 1 일 경우 (**)
        cnt += 1
        break

    if a[0] + a[-1] > k :  # limit 보다 크다
        a.pop()
        cnt += 1
    else :
        a.pop()
        a.pop(0)
        cnt += 1

print(cnt)

