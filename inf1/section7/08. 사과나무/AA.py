import sys
from collections import deque

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

n = int(input())  # n
dx = [-1, 0, 1, 0]   # 12시, 3시, 6시, 9시
dy = [0, 1, 0, -1]

a = []
for _ in range(n):
    a_in = list(map(int, input().split()))
    a.append(a_in)
#print(a)

ch = [[0]*n for _ in range(n)]   # 방문 했는지 안 했는지 체크
#print(ch)
sum = 0  # 총합
Q = deque()
ch[n//2][n//2] = 1   # 중앙지점, 방문했다고 chk
sum += a[n//2][n//2]   # sum 에 누적
Q.append((n//2, n//2))
L = 0   # 레벨 0
while True :
    if L == n//2 :   # lvl 2 -> 목표지점에 옴
        break
    size = len(Q)
    for i in range(size) :
        tmp = Q.popleft()
        for j in range(4) :   # 4 방향
            x = tmp[0] + dx[j]   # 튜플로 넣었으므로 [0]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0 :
                sum += a[x][y]
                ch[x][y] = 1
                Q.append((x, y))

    # print(L, size)
    # for x in ch :
    #     print(x)
    L += 1
print(sum)
