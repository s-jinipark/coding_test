import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(x) :
    if x == 0 :
        return
    else :
        #print(x%2, end=' ')
        DFS(x//2)
        print(x%2, end=' ') # 거꾸로 출력 (*)


if __name__ == "__main__" :
    n = int(input())
    DFS(n)
