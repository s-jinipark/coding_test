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
    # 3. 파이썬스러운 방법
    rev = s[::-1]
    #print(rev)
    sam = True
    # 비교
    #print('test1 : ' , len(s)/2)
    #print('test2 : ' , len(s)//2)  # 몫을 구하면 int() 없어도 됨
    for j in range(int(len(s)/2)):  # 반 만 loop
        #print(s[j])
        #print(rev[j])
        if s[j] != rev[j] :
            sam = False
            break
    #print(sam)
    if sam :
        print('#'+str(i+1)+" YES")
    else :
        print('#'+str(i+1)+" NO")