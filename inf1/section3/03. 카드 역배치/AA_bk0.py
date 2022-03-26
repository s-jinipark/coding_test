import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

# 카드 준비
cards = []
for k in range(20):
    cards.append(k+1)
#print(cards)

# 10 회로 가정
for i in range(10) :
    n, k = map(int, input().split())
    #print(n,k)

    cnt = 1
    for j in range(n-1, k):   # 인덱스에 +1 ... 고려
        tmp = -1
        #print(cards[j], cards[k-cnt], k-n)

        if cnt-1 > int((k-n)/2) :   # 반 만 loop
            break
        else :
            tmp = cards[j]
            cards[j] = cards[k-cnt]
            cards[k - cnt] = tmp
        cnt += 1
    #print(i+1, cards)
for k in cards :
    print(k, end=' ')

