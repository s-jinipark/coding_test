import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

n = int(input())  # N 명
#n, k = map(int, input().split())
a = list(map(int, input().split()))
# str 로
#a = list(map(str, input().split()))

def reverse(x):
    tmp = str(x)
    first_0 = True
    rtn_val = ''
    #print(tmp)
    for c in range(len(tmp)-1, -1, -1):  # 마이너스 주의!
        #print(tmp[c])
    # for i in reversed(range(len(tmp))) :
    #     print(i)
        if first_0 and tmp[c] == '0' :  # 앞자리 0
            first_0 = True
        else :
            first_0 = False
            rtn_val += tmp[c]
    return int(rtn_val)

def isPrime(x) :
    for i in range(2, x+1):
        if x%i == 0 :
            #print(x, i)
            if x > i :
                return False
                break
            else :
                return True

def reverse2(x) :
    res = 0
    while x > 0 :
        t = x % 10
        res = res*10 + t
        x = x//10
        #print('x : ', x, ' t : ', t, ' res : ', res)
    return res

def isPrime2(x) :
    if x == 1 :
        return False

    for i in range(2, x//2+1):  # 절반만 돌면 된다
        if x%i == 0 :
            return False
    else :                  # for ~ else 활용
            return True

for i in range(n) :
    #print(reverse(a[i]))
    #print(reverse2(a[i]))
    tmp = reverse(a[i])
    #print(isPrime(tmp))
    if isPrime(tmp) :
        print(tmp, end=' ')

    tmp = reverse2(a[i])
    #print(isPrime(tmp))
    if isPrime2(tmp) :
        print(tmp, end=' ')