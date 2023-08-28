'''
문제
3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

입력
첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.

출력
첫째 줄에 경우의 수를 출력한다.
'''

## method
def sol(n):
    if n%2 == 1 :
        return 0
    
    dp = [0 if i != 0 else 1 for i in range( (n//2) + 1 ) ] # 15
    
    for i in range(1,(n//2) + 1):
        if i == 1 : 
            dp[i] = 3 # 2개일 때 : 3가지
        else :
            dp[i] = 3 * dp[i-1] + 2 * (sum(dp[ : i-1 ]))

    return dp[-1]

## input
n = int(input())
## output
print(sol(n))