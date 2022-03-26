import sys

def DFS1() :
    cnt =3
    print(cnt)

def DFS2() :
    global cnt
    if cnt == 5 :
        cnt = cnt +1  # ' cnt = ' 여기서 로컬 변수 됨
        print(cnt)    # 따로 사용할거면 global 써 줌

if __name__ == "__main__" :
    cnt = 5
    DFS1()
    DFS2()
    print(cnt)
