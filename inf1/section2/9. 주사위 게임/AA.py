import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

'''
규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
'''

res = 0
for i in range(n) :
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)  # 3개 값에 넣는다는...
    print( a, b, c )

    if a ==b and b==c :  # 3 개 다 같은 거 (좋은 거 먼저??)
        money = 10000+a*1000
    elif a == b or a == c :  # a 로 계산하려고 (이게 먼저 나오면 3개 같을 때 pass 됨)
        money = 1000+(a*100)
    elif b == c :
        money = 1000+(b*100)   # b눈(?) 으로 계산
    else :
        money = c *100   # sort 되어 있으므로

    if money > res :
        res = money

print(res)