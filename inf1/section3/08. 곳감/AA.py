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
#b = [list(map(int, input().split())) for _ in range(m)]

'''
첫 번째 수는 행번호, 
두 번째 수는 방향인데 0 이면 왼쪽, 1 이면 오른쪽이고, 
세 번째 수는 회전하는 격자의 수입니다.
'''

# 하나씩 인덱스를 계산해서 tmp 에 넣었다가 옮겨 주었는데
# pop() 을 이용

for i in range(m):

    h, t, k = map(int, input().split())
    print(a[h-1])
    if t==1:  # 오른쪽
        for _ in range(k):
            #print(a[h-1].pop(0))
            a[h-1].insert(0, a[h-1].pop() )
            '''
            1이면  19 13 30 13 19  를
                   (i) (i) 19 13 30 (p) (p)  -> (뒤를 pop 해서 앞에 insert)
                   뒤에서 뺀 19 , 13 을 앞에 붙인다는
                [19, 13, 30, 13, 19]
                ->  [13, 19, 19, 13, 30]
            '''
    else :  # 왼쪽
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
            '''
            0이면          12 39 30 23 11  를
                 (p) (p) (p) 19 13 30 (a) (a) (a) -> (앞을 pop 해서 뒤에 append)
                   뒤에서 뺀 19 , 13 을 앞에 붙인다는
                [12, 39, 30, 23, 11]
                ->  [23, 11, 12, 39, 30]
            '''
    print('-> ', a[h-1])