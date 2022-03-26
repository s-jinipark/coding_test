import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

n = input()
only_num = ''

for i in range(len(n)) :
    if n[i].isdecimal() :  # 0~9 확인
        only_num += n[i]

print(int(only_num))
num = int(only_num)
cnt = 0
# 약수
for i in range(1, num+1):
    if num % i == 0 :
        cnt += 1
print(cnt)

'''
먼저 약수를 구하기 위해 입력 받은 수까지 반복문을 돌립니다.

여기서 num+1 을 하는 이유는 1 부터 20보다 작을 때까지이니 20은 반복하지 않기 때문에 +1을 해줍니다

if문으로 20 % 1 == 0 인지 체크를 하고 약수인지 판단을 합니다.
'''
