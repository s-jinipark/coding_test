import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(L) :
    global cnt
    if L == m :
        # if res[0] == res[1] :
        #     return
        priv = -1
        flag = False
        for i in range(m):
            if i > 0 and priv == res[i] :
                flag = True
            priv = res[i]
        else :
            if flag :
                return

        #print(res)
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
    else :
        for i in range(1, n+1) :  # 1,2,3
            res[L] = i
            DFS(L+1)

if __name__ == "__main__" :
    #n = int(input())
    n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    cnt = 0
    res = [0]*m
    DFS(0)
    print(cnt)
    
'''
Case #01 : Success
Case #02 : Wrong Answer
Case #03 : Success
Case #04 : Wrong Answer
Case #05 : Wrong Answer
'''