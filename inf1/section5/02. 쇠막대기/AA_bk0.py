import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))
s = input()

print(s)
stack =[]
cnt = 0

for i in range(len(s)) :
    if s[i] == ")" :
        stack.pop()
        cnt += 1
    else :
        stack.append(s[i])
print(cnt)