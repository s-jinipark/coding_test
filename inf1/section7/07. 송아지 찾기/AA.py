import sys
from collections import deque

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
n, m = map(int, input().split())  # 현수의 위치 (n)와 송아지의 위치 (m) 가 주어진다
#a = list(map(int, input().split()))
MAX = 10000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
ch[n] = 1  # check
dis[n] = 0  # 출발점이므로 0
dQ = deque()
dQ.append(n)
while dQ :
    now = dQ.popleft()
    if now == m :
        break
    for next in (now-1, now+1, now+5) :  # 3 바퀴
        if 0 < next <= MAX :
            if ch[next] == 0 :
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now]+1  # plus 1 ?
print(dis[m])
