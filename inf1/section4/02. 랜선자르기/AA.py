import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def count1(len):
    cnt = 0
    for x in a :
        cnt += (x//len)
    return cnt

#n = int(input())  # N 명
n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

a = [int(input()) for _ in range(n)]
print(a)
print(max(a))

largest = max(a)
lt = 1
rt = largest
res = 0

while lt <= rt :
    mid = (lt+rt)//2
    print(mid, count1(mid))
    if count1(mid) >= k :  # 만들 수 있는 갯수
        #print(mid, k)
        res = mid
        lt = mid+1
    else :  # 길어서 답이 안되니
        rt = mid-1
print(res)
'''
결정 알고리즘
(특징) 몇부터 몇사이 이다 (범위가 있다)
=> 좁혀나감

4 개를 11 개로 자는다
802
743
457
539

가장 큰 랜선 => 802
이것보다 길진 않다

범위를 1 ~ 1000 정도로 넉넉하게
중간값 500 -> 이걸로 자르면 3개 나옴
줄여야 함 => 범위를 1 ~ 499 로 하고
중간값 250 -> 8 개 나옴
..
다시 범위 1 ~ 249 , 중간값 125 -> 18 개
(11개를 만족하니까)
126 ~ 249 , 중간값 187 -> ..

계속진행하면서 가장 끝값 찾는다

'''
'''
(실행결과)
[802, 743, 457, 539]
802
401 5   (찾아가는 과정)
200 11
300 6
250 8
225 10
212 10
206 10
203 10
201 10
200

'''

