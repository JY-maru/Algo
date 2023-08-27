## 행렬 제곱 : G4


'''
문제
크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

입력
첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)

둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.
'''
## method
def sol(b):
    if expo[b] != [] : return expo[b]
    else :
        half = sol(b>>1)
        res = mul(half,half)
        if b%2 == 1:
            res = mul(res,expo[1])
        expo[b] = res
        return expo[b]

def mul(m1,m2):
    global N
    
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += (m1[i][k]*m2[k][j])
            res[i][j] %= 1000
    return res

## input
from collections import defaultdict
N, B = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
expo = defaultdict(list)
for i in range(N):
    for j in range(N):
        matrix[i][j]%=1000
expo[1] = matrix
## output
for e in sol(B):
    print(*e)
               
# res = [[0]*N for _ in range(N)]
# m1 = expo[1]
# m2 = expo[1]
# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             res[i][j] += (m1[i][k]*m2[k][j])%1000
# print(res)
# 00 01 02 * 00 10 20 i k * k j
# 00 01 02 * 01 11 21 
# 00 01 02 * 02 12 22 