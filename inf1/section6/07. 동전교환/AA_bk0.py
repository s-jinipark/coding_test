import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(L) :
    return

if __name__ == "__main__" :
    n = int(input())
    #n, m = map(int, input().split())
    a = list(map(int, input().split()))
    l = int(input())
    cnt =0

    a.sort(reverse=True)
    #print(a)
    for x in a :
        cnt += l //x
        l = l%x
    print(cnt)
    
'''
하나 틀림
Case #01 : Success
Case #02 : Success
Case #03 : Wrong Answer
Case #04 : Success
Case #05 : Success
'''