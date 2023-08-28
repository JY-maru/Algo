# 타일 채우기 3
'''
문제
2×N 크기의 벽을 2×1, 1×2, 1×1 크기의 타일로 채우는 경우의 수를 구해보자.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000,000)이 주어진다.

출력
첫째 줄에 경우의 수를 1,000,000,007로 나눈 나머지를 출력한다.
'''
## method
def sol(n):
    dp = [0,2,7] + [0]*(n-2)
    if n < 3 : return dp[n]
    
    MOD = int(1e9+7)
    cache = 2
    for i in range(3,n+1):
        dp[i] = (2*dp[i-1] + 3*dp[i-2] + cache)%MOD
        cache += 2*dp[i-2]
    return dp[-1]

## input
N = int(input())
## output
print(sol(N))