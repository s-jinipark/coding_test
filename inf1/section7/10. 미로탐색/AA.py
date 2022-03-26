import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

dx = [-1, 0, 1, 0]  # 12시, 3시, 6시, 9시
dy = [0, 1, 0, -1]

def DFS(x, y) :
    global cnt
    if x ==6 and y ==6 :
        cnt += 1
    else :
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= 6 and 0 <= yy <= 6 and board[xx][yy] == 0 :
                # 0 ~ 6 을 넘지 않고, 방문하지 않았어야..
                board[xx][yy] = 1
                DFS(xx, yy)
                board[xx][yy] = 0   # 뒤로 백, 주의!

if __name__ == "__main__" :

    n = 7  # 7*7 격자판
    cnt = 0

    board = []
    for _ in range(n):
        a = list(map(int, input().split()))
        board.append(a)
    print(board)
    board[0][0] = 1  # 방문 한 곳
    DFS(0, 0)

    print(cnt)
