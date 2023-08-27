'''피보나치 수 6 : G2

문제
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 n번째 피보나치 수를 1,000,000,007으로 나눈 나머지를 출력한다.
'''

## method
def F(num):
    if num <= 2:
        return memo[num]
    
    # 중복 연산 막음
    elif memo[num] > 0:
        return memo[num]
    
    # 해시값 존재 안할 시 최소 한번은 연산해주어야 함.
    else :
        half = num //2
        if num % 2 == 0 :
            h0 = F(half)
            h1 = F(half-1)
            memo[num] = ((2*h1 + h0)*h0)%1000000007
            return memo[num]
        else : 
            h0 = F(half+1)
            h1 = F(half)
            memo[num] = (h0**2 + h1**2)%1000000007
            return memo[num]
            
## input
from collections import defaultdict
n = int(input())
memo = defaultdict(int)
memo[1],memo[2] = 1,1
## output
print(F(n))

