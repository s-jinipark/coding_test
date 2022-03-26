import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(L, sum) :
    if L == n :
        if sum == (total-sum):
            print("YES")
            sys.exit(0)
    else :
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)
        print(L+1, sum, sum+a[L])

if __name__ == "__main__" :
    n = int(input())
    a = list(map(int, input().split()))
    total=sum(a)
    DFS(0, 0)
