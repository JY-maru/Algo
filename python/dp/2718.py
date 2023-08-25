# 타일 채우기
'''
문제
4*N 크기의 타일을 2*1, 1*2 크기의 도미노로 완전히 채우려고 한다. 예를 들어 4*2 타일을 채우는 방법은 다음과 같이 5가지가 있다.



N이 주어졌을 때, 타일을 채우는 방법의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 1,000보다 작거나 같은 자연수이다. 각 테스트 케이스는 정수 하나로 이루어져 있다. 이 정수는 문제에서 설명한 타일의 너비 N이다. N은 자연수이다.

N은 타일을 채우는 경우의 수가 2,147,483,647 이하이도록 주어진다.

출력
각 테스트 케이스에 대해 4*N크기의 타일을 채우는 방법의 경우의 수를 출력한다.
'''

# method
def sol(n):
    dp = [1,1,5] + [0]*(n-2)

    if n < 3 : return dp[n]
    
    cache = [5,2] 

    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]*4 + cache[i%2]
        cache[i%2] += dp[i-1]*2 + dp[i-2]*3
        
    return dp[-1]
# input
import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    # output
    print(sol(int(input())))