import sys
from collections import deque

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
n, k = map(int, input().split())
a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

print(n, k)
print(a)
# *** 튜플 자료 구조로
Q = [(pos, val) for pos, val in enumerate(a)]
print(Q)
Q = deque(Q)
cnt = 0
while True :
    cur = Q.popleft()
    # 대기 목록 뒤를 확인
    if any(cur[1]<x[1] for x in Q) :  # x로 접근 (이 구문은 외워야 할 듯)
        Q.append(cur)
    else :
        cnt += 1  # 진료 받는다
        if cur[0] == k :  # 위에서 지정한 k 번째 사람 ?
            print(cnt)
            break

'''
우선순위가 낮으면 뒤로 보내는데, 위치를 기억하고 있어야 하나?
sort 해서 하면 안되는게, 같은 위험도가 있기 때문에

index, value 로 저장
Q = [(pos, val) for pos, val in enumerate(a)]
출력
[(0, 60), (1, 50), (2, 70), (3, 80), (4, 90)]

'''