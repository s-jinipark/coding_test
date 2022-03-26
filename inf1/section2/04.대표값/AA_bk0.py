import sys
#sys.stdin = open("input.txt", "rt")  # 채점 전 주석 처리

n = int(input())  # N 명
a = list(map(int, input().split()))

# 평균 구하기
sum = 0
avg = 0
#dif = 999   # 차이
# 이부분 !! -> 파이썬에서 가장 큰 값으로
#dif = float('inf')
dif = 2147000000
scr = 0   # 중간 점수
num = 0     # 번호 출력

for i in a :
    sum += i
avg = round(sum/n)
#print(sum, avg)

for j in range(n) :
    #print(abs(avg - a[j]))
    if dif >= abs(avg - a[j]) :  # 평균과의 차이가 작은 경우 (절대값으로)
        #print(abs(avg - a[j]))
        if scr < a[j] : # 차이가 동률이면 큰 스코어 우대!
            dif = abs(avg - a[j])
            scr = a[j]
            num = j+1  # 주의 ! : 0부터 시작이므로 +1
print(avg, num)
