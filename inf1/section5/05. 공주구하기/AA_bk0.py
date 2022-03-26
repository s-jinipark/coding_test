import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

#print(n, k)
prince = []

for i in range(n) :
    prince.append(i+1)

#print(prince)
start = 0

while len(prince) > 1 :
    tmp = start + k -1
    #print(tmp, len(prince))
    if tmp >= len(prince) :
        tmp = tmp % len(prince)
    #print('>', tmp)
    prince.pop(tmp)
    start = tmp
    #print(prince)
print(prince[0])