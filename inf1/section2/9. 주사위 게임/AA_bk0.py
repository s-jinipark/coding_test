import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

def getNum(n, a):
    rtn_val = -1
    rtn_won = 0
    if n == 2 :
        prv = -1
        for i in a :
            if prv == i :
                #print(i)
                rtn_val = i
            prv = i
        rtn_won = rtn_val * 100
    elif n == 1  :
        rtn_val = max(a)
        rtn_won = 1000 + (rtn_val) * 100
    elif n == 3 :
        rtn_val = max(a)
        rtn_won = 10000 + (rtn_val) * 1000
    return rtn_won
'''
규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
'''

max_val = -1
for i in range(n) :
    a = list(map(int, input().split()))
    #print(a)
    priv = 0
    seq = 1
    for j in a :
        #print(j)
        if priv == j :
            seq += 1
        priv = j
    #print(seq, priv, getNum(seq, a))
    tmp = getNum(seq, a)
    if max_val < tmp :
        max_val = tmp

print(max_val)