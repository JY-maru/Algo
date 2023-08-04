'''
https://www.acmicpc.net/problem/15686
'''

## method
def sol(n, m, city):
    import itertools
    
    house_coor = [(i,j) for i in range(n) for j in range(n) if city[i][j] == 1 ]
    chicken_coor = [(i,j) for i in range(n) for j in range(n) if city[i][j] == 2 ]
    
    answer = 0
    
    chicken_cases = list(itertools.combinations(chicken_coor,m))
    for case in chicken_cases:
        shortest_dist = [[0]*n for _ in range(n)] # 경우의 수마다 초기화
        for cx, cy in case:
            for hx,hy in house_coor:
                distance = abs(cx-hx) + abs(cy-hy)
                if shortest_dist[hx][hy] == 0:
                    shortest_dist[hx][hy] = distance
                        
                if shortest_dist[hx][hy] > distance:
                    shortest_dist[hx][hy] = distance
            if answer == 0 :
                answer = sum([ sum(s) for s in shortest_dist])
            else:
                answer = min (answer,sum([ sum(s) for s in shortest_dist]))
            
    return answer
## input
import sys
put = sys.stdin.readline
n,m = map(int,put().split())
city = [list(map(int, put().split())) for _ in range(n)]

## output
print(sol(n,m,city))