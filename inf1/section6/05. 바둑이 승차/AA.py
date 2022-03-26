import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(L, sum) :
    global big
    if L == n :   # 마지막이란 거.
        if c >= sum :
            if big < sum :
                #print(sum)
                big = sum
                #sys.exit(0)
    else :
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)
        #print(L+1, sum, sum+a[L])

if __name__ == "__main__" :
    #n = int(input())
    c, n = map(int, input().split())
    a = []
    big = 0
    for _ in range(n) :
        a.append( int(input()) )
    #print(a)
    #a = [int(input()) for _ in range(n)]
    DFS(0, 0)  # 합이 같은 부분 집합과 유사하게
    print(big)