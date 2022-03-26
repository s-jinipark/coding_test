import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

s = input()
stack = []
for x in s :
    if x.isdecimal() :
        stack.append(int(x))   # int 화 시켜서.. 넣어줌
    else :
        if x == '+' :
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2+n1)
        elif x == '-' :
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2-n1)
        elif x == '*' :
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2*n1)
        elif x == '/' :
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2/n1)
print(stack[0])
