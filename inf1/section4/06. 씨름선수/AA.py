import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")


n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

#a = [int(input()) for _ in range(n)]

runner = []
for i in range(n):
   hi, we = map(int, input().split())
   runner.append((hi, we))   # 튜플 형태로 저장
runner.sort()
#runner.sort(key=lambda  x : (x[1], x[0]))
#print(runner)
cur_we = 0
cnt = 0
# for hi, we in runner :   # 키 순
#    if we > cur_we :  # 키 순서인 와중에
#       cur_we = we
#       cnt += 1

# [2]
maxx = 0
runner.sort(reverse=True)  # 내림차순 정렬
#print(runner)
for we in runner :
   #print(we[1])
   if maxx < we[1] :
      maxx = we[1]
      cnt +=1

print(cnt)
'''
for we in runner : -> 이렇게 받고
we[1] -> 이렇게 참조했는데

(*)
for x, y in runner :  => 이렇게 두개 받는다

'''
'''
비슷한 유형의 문제를 풀이한다는 점에서 서로 비교 대상이 되기도 하는데, 
그리디 알고리즘은 항상 그 순간에 최적이라고 생각되는 것을 선택하면서 풀이해 나가는 것이고, 
다이나믹 프로그래밍은 중복된 하위 문제들의 결과를 저장해뒀다가 풀이해 나간다는 차이가 있다.
'''

