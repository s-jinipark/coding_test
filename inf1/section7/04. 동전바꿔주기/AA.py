import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(L, sum) :
    global cnt
    if sum > t :
        return
    if L == k :  # 말단 노드
        if sum == t : # 합이 같은 경우
            cnt +=1
    else :
        for i in range(lst_cnt[L]+1):  # +1 해야 그 값까지 돈다
            DFS(L+1, sum + (lst_val[L] * i) )

if __name__ == "__main__" :
    #n, m = map(int, input().split())
    t = int(input())  # 지폐의 금액 T(0<T≤10,000)
    k = int(input())  # 동전의 가지 수 k(0<k≤10)

    lst_val = []
    lst_cnt = []
    cnt = 0
    for i in range(k) :
        a, b = map(int, input().split())
        lst_val.append(a)   # 금액
        lst_cnt.append(b)   # 갯수

    DFS(0, 0)
    print(cnt)
