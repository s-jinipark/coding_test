import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(v) :
    global cnt
    if v == n :
        cnt += 1
        # [2]-->
        for x in path :
            print(x, end=' ')
        print()
        # //<--[2]
    else :  # 가지 뻗는 거..
        for i in range(1, n+1):
            if g[v][i]==1 and chk[i]==0 :
                chk[i] = 1
                # [2]-->
                path.append(i)
                # //<--[2]
                DFS(i)
                # [2]-->
                path.pop()
                # //<--[2]
                chk[i] = 0

if __name__ == "__main__" :
    n, m = map(int, input().split())  # 정점의 수 N(2<=N<=20)와 간선의 수 M
    g = [[0] * (n+1) for _ in range(n+1)]
    chk = [0] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    # [2] 경로 확인 -->
    path = []
    path.append(1)
    # //<--[2]
    chk[1] =1
    DFS(1)
    print(cnt)
    
