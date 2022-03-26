import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

n = int(input())  # N 명
#n, m = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

a = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        #print(a[i][j])
        cur = a[i][j]
        bong = True
        # 동서남북 (순서대로)
        if j + 1 < n:
            if cur <= a[i][j+1] :
                bong = False
        if j - 1 >= 0:
            if cur <= a[i][j-1]:
                bong = False
        if i+1 < n :
            if cur <= a[i+1][j]:
                bong = False
        if i-1 >= 0 :
            if cur <= a[i-1][j]:
                bong = False
        #print(bong)
        if bong :
            cnt += 1
print(cnt)

# if ~ elif 로 했더니 잘못 나옴