import sys
from collections import deque
# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

#print(n, k)
dq = list(range(1, n+1))
print(dq)
dq = deque(dq)  # deque 가 된 거

while dq :
    for _ in range(k-1) :
        cur = dq.popleft()
        dq.append(cur)  # 앞에서 빼서 뒤로 넣은 것
    dq.popleft()  # k번째는 그냥 뺌
    if len(dq) == 1 :
        print(dq[0])
        dq.popleft()

'''
FIFO (First In First Out)
python 의 deque
 appenleft  --- append
 popleft    --- pop
 
'''