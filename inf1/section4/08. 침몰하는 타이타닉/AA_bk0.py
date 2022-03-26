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
while lt < rt :
    if a[lt] + a[rt] > k :   # 기준을 넘어 버린다
        rt -= 1   # 한 명만 포함
        cnt += 1
    else :   # 기준을 안 넘으니 2 명 갈 수 있다
        rt -= 1
        lt += 1
        cnt += 1
print(cnt)

'''
Case #01 : Success
Case #02 : Success
Case #03 : Wrong Answer
Case #04 : Success
Case #05 : Wrong Answer

점수 결과 : 60
'''
