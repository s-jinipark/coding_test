import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

n = int(input())  # N 명
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

for i in range(n) :
    s = input()
    #print(s)
    s = s.lower()
    # reverse 안쓰고
    sam = True
    # 비교
    for j in range(int(len(s)/2)):  # 반 만 loop (몫을 구함)
        #print(s[j], s[-1-j])
        if s[j] != s[-1-j] :
            sam = False
            break
    if sam :
        print('#'+str(i+1)+" YES")
    else :
        print('#'+str(i+1)+" NO")