#최소힙
#heapify이후 heappush시 NameError가 떴다.
#잦은 입력 받을 시 input() -> sys.stdin.readline()일 때 시간을 더 절약할 수 있었다.
import sys
import heapq

num = int(input())
min_heap = []

for _ in range(num):
    input_num = int(sys.stdin.readline())
    if input_num == 0:
        try :
            print(heapq.heappop(min_heap))
        except :
            print(0)
    else :
        heapq.heappush(min_heap,input_num)


