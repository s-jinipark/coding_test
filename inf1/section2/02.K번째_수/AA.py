import sys
sys.stdin = open("input.txt", "rt")  # 채점 전 주석 처리
t = int(input())  # 케이스가 몇개 인지..
for i in range(t):
    n, s, e, k = map(int, input().split())
    #print(n,s,e,k)

    #print(list(input()))  # 공백 포함되서 안됨
    a = list(map(int, input().split()))
    #print(a)
    tmp = a[s-1:e]
    tmp.sort()
    #print(tmp)
    print("#", i+1, tmp[k-1])

