import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

n = int(input())  # N 명
#n, m = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())  # N 명
b = [list(map(int, input().split())) for _ in range(m)]

#print(a)
#print(b)

for i in range(m):
    '''
    첫 번째 수는 행번호, 
    두 번째 수는 방향인데 0 이면 왼쪽, 1 이면 오른쪽이고, 
    세 번째 수는 회전하는 격자의 수입니다.
    '''
    print(b[i])
    no1, no2, no3 = b[i]
    #print(no1, no2, no3)
    tmp_list = [0] *n
    #print(tmp_list)
    print(a[no1-1] )
    for j in range(n):
        if no2 == 1 :
            # 오른쪽
            #print(j, no3 + j)
            tmp = no3 + j
            if tmp >= n:
                tmp = abs(n-tmp)
            #print(j, '->', tmp)
            tmp_list[tmp] = a[no1 - 1][j]
        else :
            # 왼쪽
            #print(j, j-no3)
            tmp = j - no3
            if tmp <0 :
                #print(n-abs(tmp))
                tmp = n-abs(tmp)
            #print(j, '->', tmp)
            tmp_list[tmp] = a[no1-1][j]
            #print( a[no1-1][j])
    print(tmp_list)
    a[no1-1] = tmp_list

#print(a)

# 모래시계 계산
tot = 0
s = 0
e = n

for i in range(n):
    for j in range(s, e):
        #print(a[i][j] , end=' ')
        tot += a[i][j]
    if i < n//2 :
        s += 1
        e -= 1
    else :
        s -= 1
        e += 1
    #print()
print(tot)
