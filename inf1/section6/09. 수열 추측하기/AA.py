import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(L, sum) :
    if L==n and sum == f :
        for x in p:
            print(x, end=' ')
        #print()
        sys.exit(0)
    else :
        for i in range(1, n+1) :
            if ch[i] ==  0 :
                ch[i] =1    # 사용 chk
                p[L] =i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i] =0

if __name__ == "__main__" :
    #n = int(input())
    n, f = map(int, input().split())
    #a = list(map(int, input().split()))
    p = [0]*n   #
    b = [1]*n   # 이항 계수
    ch = [0] * (n+1)  # 중복 관련 체크
    for i in range(1, n):
        b[i]=b[i-1]*(n-i)//i
    # for x in b:
    #     print(x, end=' ')
    DFS(0, 0)
