import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

# 2 회로 가정
n1 = int(input())
a1 = list(map(int, input().split()))
n2 = int(input())
b2 = list(map(int, input().split()))

p1 = p2 = 0  # 참조할 포인터 만듬
c = [] # 결과 list
while p1<n1 and p2<n2 : # a, b 중 한쪽이 마지막이 되면 멈춤
    if a1[p1] <= b2[p2] :
        c.append(a1[p1])
        p1 += 1
    else :
        c.append(b2[p2])
        p2 += 1
        
print(p1,p2)
print(c)

if p1<n1:
    c = c+a1[p1:]
if p2<n2:
    c = c+b2[p2:]
print(c)