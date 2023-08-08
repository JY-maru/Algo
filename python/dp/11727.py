'''
문제
2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×17 직사각형을 채운 한가지 예이다.



입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
'''

# 1 : 1
# 2 : 3 (특수 : 2)
# 3 : 2+1 1+2 = dp2+dp1*2
# 4 : 3+1 2+2 1+3 

## method
def sol(n):
    dp = [1,1,3] +[0]*(n-2)

    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]*2

    return dp[n]%10007
## input
n = int(input())
## output
print(sol(n))