import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

n = int(input())  # N 명
#n, m = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

a = [list(map(int, input().split())) for _ in range(n)]

print(a)

res = 0  # 합
s = e = n//2   # 문제에서 n 은 항상 홀수, 몫을 구하면 index 상 중간 값이 나옴

for i in range(n):
    for j in range(s, e+1):  # start , end
        res += a[i][j]
        print(i, j , a[i][j])
    # 주의 - 바깥쪽 for 문 
    if i<n//2 :
        s -= 1
        e += 1
    else :
        s += 1
        e -= 1
print(res)

'''
규칙
행  1   열  3
행  2   열  2 3 4
행  3   열  1 2 3 4 5
행  4   열  2 3 4
행  5   열  3

행이 증가하면서 열의 시작값은 -1, 끝값은 +1씩 변화하다
가운데를 기준으로 반대부터는 시작값이 +1, 끝값은 -1씩 변화하는 걸 알 수 있습니다. 
'''