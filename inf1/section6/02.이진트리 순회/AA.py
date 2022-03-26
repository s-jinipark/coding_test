import sys

# 채점 전 주석 처리
#sys.stdin = open("input.txt", "rt")

def DFS(v) :
    if v > 7 :  # if ~ else 이런 패턴으로 ..
        return
    else :
        #print(v)  # 함수 본연의 일이라 했을 때 (전위 순회)
        DFS(v*2)
        #print(v)  # 여기에 두면  (중위 순회)
        DFS(v*2+1)
        print(v)  # 여기에 두면  (후위 순회)
                    # 병합 정렬의 경우 (대부분은 전위 순회)

if __name__ == "__main__" :
    DFS(1)
