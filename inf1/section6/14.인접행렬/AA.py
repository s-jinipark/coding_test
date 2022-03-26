import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(L, S, sum) :
    return

if __name__ == "__main__" :
    n, m = map(int, input().split())  # 정점의 수 N(2<=N<=20)와 간선의 수 M
    # 행렬 만듬
    g = []
    for i in range(n):
        tmp = [0]*n
        g.append(tmp)
    #print(g)

    for i in range(m):
        a = list(map(int, input().split()))
        print(a)
        g[a[0]-1][a[1]-1] = a[2]
    print(g)

    # 출력
    for i in range(n):
        for j in range(n):
            print(g[i][j], end=' ')
        print()