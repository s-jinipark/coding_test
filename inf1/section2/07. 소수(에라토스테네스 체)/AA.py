import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")


n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

ch =[0]*(n+1)  # 20 입력이면 21 개 만듬
#print(ch)
cnt = 0
for i in range(2, n+1):  # 인덱스로 가다 보니..
    if ch[i] == 0 :
        cnt += 1
        for j in range(i, n+1, i):  # 해당 수의 배수 모두 1 로
            ch[j] = 1
'''
for 문 돌면서
0 인 경우 카운트

카운트 후에는 해당수를 1로 바꾸고
배수도 모두 1 로 바꿈

이후 for 문에서 0 아니면
돌지도 않도록

'''
print(cnt)