import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

s = input()
lst = []
for c in s :
    lst.append(c)
#print(lst)

while len(lst) > 2 :
    for i, c  in enumerate(lst):
        if c.isdecimal() == False :
            #print(i, c)
            # a = lst[i-2]
            # b = lst[i-1]
            a = int(lst.pop(i-2))
            b = int(lst.pop(i-2))
            tmp = 0
            if c == '+' :
                tmp = a + b
            elif c == '-':
                tmp = a - b
            elif c == '*':
                tmp = a * b
            elif c == '/':
                tmp = a / b
            lst.insert(i-2, str(tmp))
            lst.pop(i - 1)
            #print('>', a, b)
            break
print(lst[0])

'''
맞기는 했으나...
스택 사용하도록 바꿔야..
'''