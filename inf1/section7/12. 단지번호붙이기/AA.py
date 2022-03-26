import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

dx = [-1, 0, 1, 0]  # 12시, 3시, 6시, 9시
dy = [0, 1, 0, -1]

def DFS(x, y) :
    global cnt
    cnt += 1
    board[x][y] = 0

    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
            DFS(xx, yy)

if __name__ == "__main__" :

    n = int(input())  # N , 지도의 크기

    board = [list(map(int, input()))  for _ in range(n)]
    res = []   # 한 단지의 집의 갯수

    for i in range(n) :
        for j in range(n) :
            if board[i][j] == 1 :
                cnt = 0   # 단지 마다
                DFS(i, j)
                res.append(cnt)

    print(len(res))
    res.sort()
    for x in res :
        print(x)
