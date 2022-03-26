import sys
from collections import deque

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))
s1 = input()
s2 = input()

# 개선된 코드
sH= dict()

for x in s1 :
    sH[x] = sH.get(x, 0) +1

for x in s2 :
    sH[x] = sH.get(x, 0) -1

for x in s1 :
    if sH.get(x) > 0 :
        print("NO")
        break
else :
    print("YES")

'''
str1 = dict()
str2 = dict()

for x in s1 :
    str1[x] = str1.get(x, 0) + 1  # x 값이 없으면 0

for x in s2:
    str2[x] = str2.get(x, 0) + 1

print(str1)
print(str2)

for i in str1.keys() :
    if i in str2.keys() :  # 당연히 str2 에도 key 가 있어야 됨
        if str1[i] != str2[i] :  # key 의 값(개수) 도 같아야 함
            print("NO")
            break
    else :
        print("NO")
        break
else :  # 정상적으로 for 문 끝난다
    print("YES")
'''

