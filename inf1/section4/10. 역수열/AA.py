import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")


n = int(input())  # N
#n, k = map(int, input().split())
a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

#a = [int(input()) for _ in range(n)]

print(a)
r_a = [0]*n
print(r_a)

# for i in range(n) :
#     tmp = a[i]  # 인덱스 0 -> 1 이란 말
#     for j in range(n) :
#         if j >= tmp and r_a[j] == 0 :
#             r_a[j] = i+1
#             break
#     print(r_a)

for i in range(n) :
    for j in range(n) :
        if a[i] == 0 and r_a[j] == 0 :  # 0 일 경우 처리 (*), 중요하다 함
            r_a[j] = i+1
            break
        elif r_a[j] == 0 :
            a[i] -= 1
    print(r_a)
