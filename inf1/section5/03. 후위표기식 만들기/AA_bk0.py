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
res = ''

for i in range(len(s)) :
    if s[i] == '*' or s[i] == '/'  :
        res += s[i]
    elif s[i] == '+'  or s[i] == '-' :
        tmp = stack[-1]
        if tmp == '*' or tmp== '/' :
            tmp = stack[-1]
    else :
        stack.append(s[i])
