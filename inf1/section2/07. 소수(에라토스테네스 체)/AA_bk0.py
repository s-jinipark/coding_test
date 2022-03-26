import sys

# 채점 전 주석 처리
#sys.stdin = open("input.txt", "rt")


n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

cnt = 0
pri = False
for i in range(2, n+1):
    pri = False
    for j in range(2,i+1):
        if i % j == 0 :
            #print(i, j)
            if i == j :
                pri = True  # 다 돌았다는 ...
                #print(i, j)
            else :
                break
    if pri :
        cnt += 1
print(cnt)
