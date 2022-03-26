import sys
sys.stdin = open("input.txt", "rt")  # 채점 전 주석 처리
n, k = map(int, input().split())
#print(n,k)
cnt = 0
for x in range(1, n+1) : # 1부터 n 까지
    if n%x == 0 : # 약수 발견
        cnt += 1
    if cnt == k :
        print(x)
        break
else :
    print(-1)