## method
def pow_matrix(n): # n : 지수승 / return -> matrix
    
    if n == 1 : return [[4,-1],[1,0]]
    elif n == 0 : return [[1,0],[0,0]]
    else :
        half = pow_matrix(n >> 1)
        if n%2 :
            return mul_matrix(mul_matrix(half,half),pow_matrix(1))
        else :
            return mul_matrix(half,half)
        
def mul_matrix(m1,m2): 
    global MOD
    res = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += ((m1[i][k] * m2[k][j]))
            res[i][j] %= MOD
    return res
## input
from collections import defaultdict
N = int(input())
MOD = int(1e9+7)

## output
if N%2 == 1: print(0)
else:
    sub = [[3,0],[1,0]] # (dp1,dp0 )

    result = pow_matrix(N//2-1)
    # 마지막에 열벡터 (3,1)을 곱할 때 모듈러 연산이 실행되지 않음.
    answer = mul_matrix(result,sub)

    print(answer[0][0])