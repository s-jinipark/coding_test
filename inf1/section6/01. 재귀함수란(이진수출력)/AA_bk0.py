import sys

# 채점 전 주석 처리
sys.stdin = open("input.txt", "rt")

def DFS(x) :
    if x > 0 :
        #print(x)
        DFS(x-1)
        print(x)   # print 를 아래로 옮기면 1 2 3 .. 순으로 출력


def makeBinary(x):
    rtn = ''
    if x > 1 :
        print(x%2)
        rtn = makeBinary(x//2)
    else :
        print(x)
        rtn = x
    return rtn

if __name__ == "__main__" :
    n = int(input())
    #DFS(n)   # 이건 테스트
    res = makeBinary(n)
print(res)
# 거꾸로 출력되므로, 변수에 담을려고 했음
# 누적해서 변수에 담기 ?  global ? 안됨


'''
재귀함수 
  - 자기 자신을 호출
  - stack 사용
  - 반복문이 효과 (대체재)
    . 3중, n중 for 문 
  
'''