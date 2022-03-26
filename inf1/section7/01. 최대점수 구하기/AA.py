import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(L, sum,  time) :
    global res
    if time > m :
        return
    if L == n :
        if sum > res :
            res = sum
    else :  # 사용 하는 쪽, 아닌 쪽
        DFS(L+1, sum+lst_val[L], time+lst_time[L])
        DFS(L+1, sum, time)

if __name__ == "__main__" :
    n, m = map(int, input().split())  # 문제의 개수N(1<=N<=20)과 제한 시간 M(10<=M<=300)

    lst_val = []
    lst_time = []

    for i in range(n):
        a, b = map(int, input().split())
        lst_val.append(a)
        lst_time.append(b)
    res = -1
    DFS(0, 0, 0)
    print(res)
