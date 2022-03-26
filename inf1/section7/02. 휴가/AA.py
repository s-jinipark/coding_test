import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(L, day,  money) :
    global res
    if L == n :
        if money > res :
            res = money
    else :  # 하는 쪽, 아닌 쪽
        if day+lst_day[L] < n :  # 중요
            DFS(L+1, day+lst_day[L], money+lst_money[L])
        DFS(L+1, day, money)

if __name__ == "__main__" :
    #n, m = map(int, input().split())
    n = int(input())  # 남은 기간

    lst_day = []
    lst_money = []

    for i in range(n):
        a, b = map(int, input().split())
        lst_day.append(a)
        lst_money.append(b)
    res = -1
    DFS(0, 0, 0)
    print(res)

'''
Case #01 : Wrong Answer
Case #02 : Wrong Answer
Case #03 : Wrong Answer
Case #04 : Wrong Answer
Case #05 : Wrong Answer

'''