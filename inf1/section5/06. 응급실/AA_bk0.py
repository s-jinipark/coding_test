import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
n, k = map(int, input().split())
a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

print(n, k)
print(a)
idx = k
cnt = 0

while a :
    tmp = a.pop(0)  # 맨 앞 꺼낸다
    idx -= 1
    print(max(a))
    if max(a) > tmp :  # 위험도 높은 사람 있는지
        a.append(tmp)  # 다시 넣어준다
        if idx == 0 :
            idx = len(a)-1
    else :
        cnt +=1
        if idx == 0 :
            break

print(cnt)

'''
우선순위가 낮으면 뒤로 보내는데, 위치를 기억하고 있어야 하나?

'''