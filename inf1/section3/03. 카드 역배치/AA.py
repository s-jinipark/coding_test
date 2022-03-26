import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

# 카드 준비
# cards = []
# for k in range(20):
#     cards.append(k+1)
cards = list(range(21))
print(cards)

for _ in range(10):  # 변수 없이 그냥 반복
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):  # 반 만 loop
        #print(cards[s+i], cards[e-i])
        cards[s + i], cards[e - i] = cards[e-i], cards[s+i]
print(cards)
cards.pop(0) # 0 빼줌
