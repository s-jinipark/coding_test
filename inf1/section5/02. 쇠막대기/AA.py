import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))
s = input()

#print(s)
stack =[]
cnt = 0

for i in range(len(s)) :
    if s[i] == ")" :
        # stack.pop()
        # cnt += 1
        # 여기서 무조건 더하지 않고 앞에 확인
        #if stack[-1] == "(" : # [1] => 이러면 레이저란 거 ...
        if s[i-1] == "(":  # => stack 에 있는 거 보지 않고 바로 앞거랑 비교 .
            stack.pop()
            cnt += len(stack)  # 여기는 레이저인 경우
        else :
            stack.pop()  # 막대기의 끝부분
            cnt += 1
    else :
        stack.append(s[i])
print(cnt)

'''
[1] 결과는
Case #01 : Success
Case #02 : Wrong Answer
Case #03 : Wrong Answer
Case #04 : Wrong Answer
Case #05 : Wrong Answer

stack 과 비교해서 () 면 레이저라 생각했는데.
그러지말고 바로 앞거랑 비교

여는 괄호 -> 스택에 넣는다
닫는 괄호 나왔을 때 바로 앞 확인(스택 말고)
스택에서 pop 하고 stack 의 길이 더한다
닫는 괄호 나와서 앞 확인 했는데 닫는 괄호(연속으로 나옴)
그러면 stack 에서 꺼내면서 +1 (막데기의 끝지점이니까.)

'''