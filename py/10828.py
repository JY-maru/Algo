#스텍
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

def sol(put):
    if put[0] == 'push':
        data.append(put[1])
    elif put[0] == 'pop':
        try : 
            print(data.pop())
        except :
            print(-1)
    elif put[0] == 'size':
        print(len(data))
    elif put[0] == 'empty':
        if data :
            print(0)
        else :
            print(1)
    elif put[0] == 'top':
        try : print(data[-1])
        except : print(-1)
#in & out
import sys
N = int(input())
data = []
for _ in range(N):
    put = sys.stdin.readline().split()
    sol(put)