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
res = ''  # 여기에 누적

for x in s :
    if x.isdecimal() :  # 피연산자인지 확인
        res += x
    else :
        if x == '(' :  # 여는 괄호 -> append
            stack.append(x)
        elif x == '*' or x == '/' :
            while stack and (stack[-1]=='*' or stack[-1]=='/') :
                res += stack.pop()  # 왼쪽이니까 다 끄집어 냄
            stack.append(x)
        elif x == '+' or x == '-' :
            while stack and stack[-1] != '(' :
                res += stack.pop()
            stack.append(x)
        elif x == ')' :
            while stack and stack[-1] != '(' :
                res += stack.pop()
            stack.pop()  # 여는 괄호 빼 준다
while stack :
    res += stack.pop()  # 남아 있는 애들 빼준다
print(res)

'''
설명을 들으면 알겠는데.
비슷한 문제를 새롭게 풀 수 있을지는 의문

'''