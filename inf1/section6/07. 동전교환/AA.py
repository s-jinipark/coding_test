import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS_try(L, sum) :  # my try
    if sum == lim :  # 합계가 같을 경우
        print(res)
        for x in a:
            res[x] = 0
        return
    elif sum > lim :
        return
    else :
        for x in a:
            print(x, sum)
            res[x] += 1
            DFS(L+1, sum+x)

def DFS(L, sum) :  # 풀이
    global res
    if L > res:  # 속도 개선을 위해 추가로.
        return
    if sum > lim :
        return
    if sum == lim :  # 합계가 같을 경우
        if L < res:
            res = L
    else :
        for i in range(n):
            DFS(L+1, sum + a[i])

if __name__ == "__main__" :
    n = int(input())
    #n, m = map(int, input().split())
    a = list(map(int, input().split()))
    lim = int(input())
    #res = {1:0, 2:0, 5:0}
    res = 2147000000
    a.sort(reverse=True)  # 5 원부터 적용할려고
    DFS(0, 0)
    print(res)