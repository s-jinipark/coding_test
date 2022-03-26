import sys
from collections import deque

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # n
n = 7   # 7*7 격자판
dx = [-1, 0, 1, 0]   # 12시, 3시, 6시, 9시
dy = [0, 1, 0, -1]

board = []
for _ in range(n):
    a = list(map(int, input().split()))
    board.append(a)
print(board)

dis = [[0]*n for _ in range(n)]   # 방문 했는지 안 했는지 체크
print(dis)

Q = deque()
Q.append((0,0))
board[0][0] = 1   # 벽으로 만드는 효과
while Q :
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y]==0:
            board[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            Q.append((x, y))
if dis[6][6] == 0 : # 도착점에 못 왔음
    print(-1)
else :
    print(dis[6][6])