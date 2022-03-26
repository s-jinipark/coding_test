import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def Count(capa):
    cnt = 1
    sum = 0
    for x in a :
        if sum+x > capa : # 곡들을 저장했을 때 누적 시간
            cnt += 1
            sum = x
        else :
            sum += x
    return cnt

#n = int(input())  # N 명
n, k = map(int, input().split())
a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

print(a)
lt =1
rt = sum(a)
res = 0
maxx = max(a) # 추가된 부분

while lt <= rt :
    mid = (lt+rt)//2
    #if Count(mid) <= k :
    if mid > maxx and Count(mid) <= k: # dvd 용량은 최소 가장 큰 노래 만큼은 되어야
        res = mid
        rt = mid -1
    else :
        lt = mid +1
print(res)

'''
lt     rt
       45 최대범위
	 
중간 23 -> 3장에 담아 낼 수 있는가?  OK (답 가능 -> res 에 저장)
23 보다 큰 용량은 당연히 됨

23//2 -> 11 => 3장 넘어 감.. X

lt 가 12 로 변하고 (12+22)//2 = 17

'''
'''
9 3
1 2 3 4 5 6 7 8 9
를
9 9
1 2 3 4 5 6 7 8 9
했을 경우 1이 나옴
고쳐서 9 나옴

'''