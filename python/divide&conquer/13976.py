# P5
'''
문제
3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000,000,000,000,000,000)이 주어진다.

출력
첫째 줄에 경우의 수를 1,000,000,007로 나눈 나머지를 출력한다.
'''
## method
def pow_matrix(n): # n : 지수승 / return -> matrix
    global MOD
    if n in (0,1) : return matrix[1]
    elif matrix[n] != []: return matrix[n]
    else :
        half = n // 2 
        if n % 2 == 1:
            m1 = pow_matrix(half)
            m2 = pow_matrix(half+1)
        else : 
            m1 = pow_matrix(half)
            m2 = pow_matrix(half)
        e00 = ((m1[0][0]*m2[0][0]) + m1[0][1]*m2[1][0])
        e01 = (m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1])
        e10 = (m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0]) 
        e11 = (m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1])

        matrix[n].append([
            e00%MOD if e00 > 0 else (-1)*(((-1)*e00)%MOD),
            e01%MOD if e01 > 0 else (-1)*(((-1)*e01)%MOD)
            ])
        matrix[n].append([
            e10%MOD if e10 > 0 else (-1)*(((-1)*e10)%MOD),
            e11%MOD if e11 > 0 else (-1)*(((-1)*e11)%MOD)
            ])
        
        return matrix[n]
## input
from collections import defaultdict
N = int(input())
matrix = defaultdict(list)
matrix[1] = [[4,-1],[1,0]]
MOD = int(1e9+7)

## output
if N%2 == 1: print(MOD)
else:
    result = pow_matrix(N//2 - 1)
    print(result)
    print(result[0][0]*3 + result[0][1])
    

