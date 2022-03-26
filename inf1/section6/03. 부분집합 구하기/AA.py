import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(x) :
    if x == n+1 :   # 종료 지점
        for i in range(1, n+1) :
            if ch[i]==1 :
                print(i, end=' ')
        print()
    else :
        ch[x] = 1   # 사용하겠다
        DFS(x+1)
        ch[x] = 0   # 사용하지 않겠다
        DFS(x+1)

if __name__ == "__main__" :
    n = int(input())
    ch =[0] * (n+1)  # chk 변수 , 사용하나/안하나
    DFS(1)

