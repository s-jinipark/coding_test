import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(L, S, sum) :
    global cnt
    if L == k :  # k 개를 뽑음
        if sum%m == 0 :
            print(sum)
            cnt += 1
    else :  # 가지 뻗는 거..
        for i in range(S, n):
            DFS(L+1, i+1, sum+a[i])

if __name__ == "__main__" :
    n, k = map(int, input().split())  # N개의 정수가 주어지면 그 숫자들 중 K개를 뽑는 조합
    a = list(map(int, input().split()))
    m = int(input())  # 조합의 합이 임의의 정수 M의 배수
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)
    
