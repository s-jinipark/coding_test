import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

n = int(input())  # N 명
#n, m = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

a = [list(map(int, input().split())) for _ in range(n)]

# 둘레에 0 을 감싼다
a.insert(0, [0]*n)
a.append([0]*n)
for x in a :
    x.insert(0,0)
    x.append(0)
# # 확인용
# for x in a :
#     print(x)
cnt = 0
# 상하 좌우 탐색 시
dx=[-1, 0, 1, 0]  # 12시, 3시, 6시, 9시
dy=[0, 1, 0, -1]
bong = True
for i in range(1, n+1):
    for j in range(1, n+1):
        print( a[i][j] )
        bong = True
        # 상하좌우 비교
        for k in range(len(dx)):
            if a[i][j] < a[i+dx[k]][j+dy[k]] :
                bong = False
        if bong :
            print(bong)
            cnt += 1
print('cnt: ' , cnt)

# 한번에 비교하도록
cnt2 = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        # 상하좌우 비교
        if all(a[i][j] > a[i+dx[k]][j+dy[k]]  for k in range(4)):
            cnt2 += 1
print('cnt2: ' , cnt2)
