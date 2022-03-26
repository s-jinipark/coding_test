import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
n, m = map(int, input().split())
a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

lt = 0
rt = 1   #rt = 0    # 0 이어서 하나 적게 나왔음
tot = a[0]
cnt = 0
'''
lt 부터 ~ rt 바로 전 자료 까지 (합)
tot < m   : rt 를 증가시키면서 더함
    =     : lt 빼주고 lt 증가 (화살표가 이동한다고 생각하면.. ), cnt 증가
    >     : 
'''
# m (지정된 수) 과 연속 부분합을 비교
while True:
    if tot < m:   # m : 지정된 수
        if rt < n:   # 전체 갯수
            tot += a[rt]  # rt -> 계속 밀고 나가면서 더함
            rt += 1
        else :
            break   # 끝 까지 감
    elif tot == m :
        cnt += 1
        tot -= a[lt]   # lt 값 빼줌
        lt += 1    # lt 증가
    else :
        tot -= a[lt]   # lt 값 빼줌
        lt += 1    # lt 증가
print(cnt)