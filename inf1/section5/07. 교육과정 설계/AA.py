import sys
from collections import deque

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))
inp = input()
n = int(input())  # N 명

for i in range(n):
    plan = input()
    dq = deque(inp)
    for x in plan :
        if x in dq :  # q 에 있는지 확인
            if x != dq.popleft() :  # 순서대로 안 되어 있다는 얘기
                print('#%d NO' %(i+1))
                break
    else :  # 다 돈 다음 남아 있는지 확인
        if len(dq) == 0 :
            print('#%d YES' %(i+1))
        else :
            print('#%d NO' %(i+1))

