import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
n, k = map(int, input().split())
a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

#print(a)
# 전제 조건은 정렬
a.sort()
#print(a)
lt = 0
rt = n-1

while lt <=rt:
    mid = (lt+rt)//2
    if a[mid] == k:  # k -> 찾는 수
        print(mid+1)  # 인덱스니까 + 1
        break
    elif a[mid] > k:
        rt = mid -1
    else :
        lt = mid +1
'''
이분 검색
lt , rt 정하고
mid = (lt + rt) //2

a[mid] == m (찾는 수?)

  작으면 : rt = mid -1
  크면  : lt = mid +1
'''
