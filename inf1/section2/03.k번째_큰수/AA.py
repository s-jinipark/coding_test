import sys
sys.stdin = open("input.txt", "rt")  # 채점 전 주석 처리

n, k = map(int, input().split())
a = list(map(int, input().split()))

# set 이라는 자료구조는 반복 제거
res = set()

# n 개중 3개 선택
for i in range(n):
    for j in range(i+1, n):
        for m in range (j+1, n):  # 마지막은 항상 n ??
            #print(i, j, m)
            res.add(a[i]+a[j]+a[m])

# sort 가 없어서 list 로 변경
res=list(res)
res.sort(reverse=True)

print(res[k-1]) # k번쟤

'''
0 1 2
~ ~
6 7 8
6 7 9
6 8 9
7 8 9
모두 n 까지로 해 놓아도
마지막에는 7 8 9 에서 끝남
'''