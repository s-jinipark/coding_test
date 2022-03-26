import heapq
import sys
import heapq as hq

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

'''
최소힙을 조금 수정

입력값에 - 부호를 붙여 줌 (부호를 반대로)
=> 최대힙 효과
'''

a = []  # 리스트 만들고
while True :
    n = int(input())
    if n == -1 :  # 입력 종료
        break
    if n == 0 :
        if len(a) == 0 :  # 힙이 비어 있다
            print(-1)
        else :
            #print(hq.heappop(a))  # root node 값임
            print(-hq.heappop(a))
    else :
        #heapq.heappush(a, n)  # n 값을 push 하라
        heapq.heappush(a, -n)

print(a)
