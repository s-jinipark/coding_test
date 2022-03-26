import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

a = [int(input()) for _ in range(n)]
print(a)

#평균값으로 시작
sum = 0
for x in a :
    sum += x
mid_val = int(sum/k)
print(mid_val)

def cut_line(mid_val, a):
    rtn_val = 0
    for x in a:   # a (list) 를 loop 돌면서 갯수 count
        rtn_val += x//mid_val
    return rtn_val

print(cut_line(mid_val, a))

cnt = 0
while True :
    cnt = cut_line(mid_val, a)
    print(mid_val, cnt)
    if k > cnt :  # mid_val 를 줄여야 된다는 ..
        mid_val -= mid_val//2
    elif k < cnt :
        mid_val += mid_val//2
    else : # 같은 경우
        break
print(mid_val)
# 최대 길이를 구해야..
while k == cnt :
    cnt = cut_line(mid_val, a)
    mid_val += 1

print(mid_val)