import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")


n = int(input())  # N
#n, k = map(int, input().split())
a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

#a = [int(input()) for _ in range(n)]


print(a)

# 처음엔 적은 수에서 시작
lt = 0
rt = n-1
res = ''
last = 0
tmp = []   # 임시 리스트에 맨앞, 맨 뒤 값을 넣고 sort

while lt <= rt :  # <= 임
    if a[lt] > last :
        tmp.append((a[lt], 'L'))  # 튜플 형태로 입력
    if a[rt] > last :
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0 :  # last 보다 작다면 끝
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L' :
            lt += 1
        else :
            rt -= 1
    tmp.clear()
print(len(res))
print(res)


