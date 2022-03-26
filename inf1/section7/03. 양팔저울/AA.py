import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(L, sum) :
    global res
    if L == n :
        if 0 < sum <=s :    # 음수는 안 본다(대칭적으로 나타남)
            res.add(sum)
    else :
        DFS(L+1, sum+G[L])  # 추를 왼쪽
        DFS(L+1, sum-G[L])  # 추를 오른쪽
        DFS(L+1, sum)

if __name__ == "__main__" :
    #n, m = map(int, input().split())
    n = int(input())  # 추의 갯수
    G = list(map(int, input().split()))
    s = sum(G)  # 추의 합

    res = set()
    DFS(0, 0)
    print(s-len(res))

'''

    ／ ｜ ＼
   ／  ｜  ＼
  ／   ｜   ＼
왼쪽 오른쪽 사용안함
'''