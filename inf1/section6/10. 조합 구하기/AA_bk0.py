import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(L, S) :
    global cnt
    if L == m :
        for i in range(L):
            print(res[i], end=' ')
        print()
        cnt+=1
    else :
        #for i in range(1, n+1):
        for i in range(S, n + 1):
            if chk[i] ==0 :
                chk[i] = 1
                res[L] =i
                DFS(L+1, S+1)
                #DFS(L + 1, i + 1)
                chk[i] = 0

if __name__ == "__main__" :
    #n = int(input())
    n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    cnt = 0
    res = [0]*m     # 08.순열 구하기 와 유사
    chk=[0]*(n+1)
    DFS(0, 1)
    print(cnt)
    
