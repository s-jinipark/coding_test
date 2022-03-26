import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(x) :
    if x == 11 :   # 종료 지점
        for i in range(1, 11) :
            if ch[i]==1 :
                print(i, end=' ')
        print()
    else :
        if x == -1 :
            return
        ch[x] = 1   # 사용하겠다
        DFS(x+1)
        ch[x] = 0   # 사용하지 않겠다
        DFS(x+1)

if __name__ == "__main__" :
    n = int(input())
    a = list(map(int, input().split()))
    ch =[-1] * 11  # chk 변수 , 사용하나/안하나
    # 일단 11 개 만들고 (앞 예제 따라서)
    print(ch)
    for x in a :
        ch[x] = 0
    print(ch)  # 사용할 것만 0 으로 셋팅
    DFS(1)

'''
각 원소를 사용하는가 사용하지 않는가로 구분
이걸 chk 변수로

'''
