import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

#n = int(input())  # N 명
n, k = map(int, input().split())
#a = list(map(int, input().split()))

dic = {}
# N * M 루핑
for n2 in range(1, n+1):
    for k2 in range(1, k+1):
        #print(n2+k2)
        tmp = n2+k2
        if tmp in dic:
            #print("있음", dic.get(tmp))
            dic[tmp] = dic.get(tmp) + 1
        else:
            dic[tmp] = 1
#print(dic)
#print(max(dic.values()))  # 딕셔너리의 value 중에 최댓값을 출력
# max함수를 이용했을 때는 value의 최댓값 중 맨 앞에 있는 key 하나만 출력
#print( max(dic,key=dic.get) )

# 리스트 컴프리핸션을 이용했을 때는 value의 최댓값에 대한 모든 key를 출력
#print(  [k for k,v in dic.items() if max(dic.values()) == v] )

#====================
#[2]
max_val = max(dic.values());
for k, v in dic.items():
    #print(k, v)
    if v == max_val :
        print(k, end=' ')

# 리스트에 담아서 order 해준 뒤 print



