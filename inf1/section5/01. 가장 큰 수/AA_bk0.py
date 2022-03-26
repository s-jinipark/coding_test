import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
n, k = map(int, input().split())
#a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

# list 만들어 역 sort 후 -> 뒤에 자르고 -> 다시 int 하면 될 듯

# tmp = str(n)
# print(tmp)
# tmp_list = []
# for c in tmp:
#     tmp_list.append(c)
# print(tmp_list)
# tmp_list.sort(reverse=True)
# print(tmp_list)
# => 이거 아님. 자리는 유지해야 함

big = 0
tmp = str(n)
tmp_list = []
for c in tmp:
    tmp_list.append(int(c))
print(tmp_list)

lt = 0
cnt = 0

while cnt < k :
    for i in range(lt, lt+k) :
        #print(type(tmp_list[i]))
        if tmp_list[i] > big :
            big = tmp_list[i]
            lt = i
        cnt += 1
        print(lt, lt+k, cnt)
print(cnt)


