import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
n, k = map(int, input().split())
a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

#print(a)
a.sort()
#print(a)

pos = n//2
while True :
    if k > a[pos] :
        pos += pos //2
    elif k < a[pos] :
        pos -= pos //2
    else : # 같은 경우
        break
#print(pos)
#위치 번호니까
print(pos+1)


'''
(채점)
Case #01 : exit_code_1
Case #02 : Success
Case #03 : Success
Case #04 : exit_code_1
Case #05 : Time Limit Exceeded

점수 결과 : 40
'''