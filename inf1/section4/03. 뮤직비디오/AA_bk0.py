import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
n, k = map(int, input().split())
a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

def check_sub_sum(x):
    # k 개로 나눌 수 있는지 chk
    s = 0
    tmp_list = [0] * k
    for i in range(k):  # 3회 실시
        tmp = 0
        for j in range(s, n):
            if tmp < x :
                tmp += a[s]
                s += 1
            else :
                break
        tmp_list[i] = tmp
    print(tmp_list)
    ok = True
    for t in tmp_list :
        if t > x :
            ok = False
    return ok

print(a)
#print(sum(a)/k)
x = sum(a)//k
#print(x)
print(check_sub_sum(x))
while True :
    if check_sub_sum(x) :
        break
    x += 1