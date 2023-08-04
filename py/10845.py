#큐 
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# DS : queue

def sol(put):
    if put[0] == 'push':
        data.append(put[1])
    elif put[0] == 'pop':
        try : 
            print(data.popleft())
        except :
            print(-1)
    elif put[0] == 'size':
        print(len(data))
    elif put[0] == 'empty':
        if data :
            print(0)
        else :
            print(1)
    elif put[0] == 'front':
        try : print(data[0])
        except : print(-1)
    elif put[0] == 'back':
        try : print(data[-1])
        except : print(-1)
#in & out

from collections import deque
import sys
N = int(input())
data = deque([])
for _ in range(N):
    put = sys.stdin.readline().split()
    sol(put)