# 정사각형
'''
문제
네 점이 주어졌을 때, 네 점을 이용해 정사각형을 만들 수 있는지 없는지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 네 줄로 이루어져 있으며, 점의 좌표가 한 줄에 하나씩 주어진다. 점의 좌표는 -100,000보다 크거나 같고, 100,000보다 작거나 같은 정수이다. 같은 점이 두 번 이상 주어지지 않는다.

출력
각 테스트 케이스마다 입력으로 주어진 네 점을 이용해서 정사각형을 만들 수 있으면 1을, 없으면 0을 출력한다.
'''

## method
def dist(coor1,coor2):
    
    import math
    x1,y1 = coor1
    x2,y2 = coor2
    return round(math.sqrt((x1-x2)**2 + (y1-y2)**2),2)
## input 
import sys
input = sys.stdin.readline
import itertools
T = int(input())
## output
for _ in range(T):
    case = [[*map(int,input().split())] for _ in range(4)]
    check = sorted([dist(i,j) for i,j in itertools.combinations(case,2)])
    # print(check)
    if check[0]==check[1]==check[2]==check[3] and check[4]==check[5]: print(1)
    else : print(0)

