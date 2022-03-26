import sys
sys.stdin = open("input.txt", "rt")  # 채점 전 주석 처리

n = int(input())  # N 명
a = list(map(int, input().split()))

# 평균 구하기
avg = round(sum(a)/n)
# 이부분 !! -> 파이썬에서 가장 큰 값으로
min = float('inf')
#min = 2147000000

for idx, x in enumerate(a) :
    tmp = abs(x-avg)
    if tmp < min :   # 적다면
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min :   # 동률일 경우
        if x > score :
            score = x   # 큰 값 우대
            res = idx + 1   # 주의 ! : 0부터 시작이므로 +1
print(avg, res)
