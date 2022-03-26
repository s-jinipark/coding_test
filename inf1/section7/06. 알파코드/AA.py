import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(L, P) :
    global cnt
    if L == n :  # 말단
        cnt += 1
        for j in range(P):
            #print(res[j], end=' ')
            print(chr(res[j]+64), end='')
        print()

    else :  # 가지 뻗는 거
        for i in range(1, 27):
            if code[L] == i :
                res[P]=i
                DFS(L+1, P+1)
            elif i >= 10 and code[L] == i//10 and code[L+1]==i%10 :
                res[P]= i
                DFS(L+2, P+1)

if __name__ == "__main__" :
    #n, m = map(int, input().split())
    code = list(map(int, input() ))
    n = len(code)

    code.insert(n, -1)  # index 오류가 나지 않도록??

    res = [0] * (n+3)
    cnt = 0

    DFS(0, 0)
    print(cnt)
