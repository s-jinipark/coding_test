import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

# tmp = str(n)
# tmp_list = []
# for c in tmp:
#     tmp_list.append(int(c))
# print(tmp_list)
# 웁스~ ! 동일한 코드
num = list(map(int, str(n)))
#print(num)
stack = []

for x in num :
    while stack and k>0 and stack[-1] < x :   # 나보다 적으면 꺼낸다
        stack.pop()
        k -= 1
    stack.append(x)
if k >0 :   # 다 지우지 못한 경우(주어진 갯수만큼 지워야 함)
    stack = stack[:-k]

for p in stack :
    print(p, end='')

'''
자기보다 앞 수가 작으면 -> 지우고 앞으로 간다
근데 지우는 횟수 제한 있음

stack : LIFO(Last In First Out)

'''