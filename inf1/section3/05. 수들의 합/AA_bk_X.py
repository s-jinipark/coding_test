import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
n, k = map(int, input().split())
a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))
cnt = 0
for i in range(n) :
    tmp = a[i]
    for j in range(i+1, n):
        if tmp == k :
            cnt += 1
            break
        elif tmp > k :
            break
        print(tmp, a[j], cnt)
        tmp += a[j]


print(cnt)