import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(L) :
    global res
    if L == n :  # 말단
        cha  = max(money) - min(money)
        if cha < res :
            tmp = set()   # 값이 다 다르다는 것 chk
            for x in money :
                tmp.add(x)
            if len(tmp) == 3 :
                res = cha

    else :  # 가지 뻗는 거
        for i in range(3):  # 3 명
            money[i] += coin[L]
            DFS(L+1)
            money[i] -= coin[L]

if __name__ == "__main__" :
    #n, m = map(int, input().split())
    n = int(input())  # 동전의 개수 N(3<=N<=12)

    coin = []
    money = [0] * 3  # 각 사람의 금액

    res = 2147000000

    for _ in range(n) :
        coin.append(int(input()))

    DFS(0)
    print(res)
