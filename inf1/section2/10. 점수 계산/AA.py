import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

n = int(input())  # N 명
#n, k = map(int, input().split())
a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

priv = -1
tot = 0
seq = 0
for i in a :
    if i == 1 :  # 정답
        # if  priv == i :
        #     seq += 1
        # tot = tot + 1 + seq
        # priv 비교 필요 없음 (헐)
        seq += 1
        tot += seq
    else :  # 오답
        seq = 0
    priv = i
    #print(i, tot, seq)

print(tot)