## 곱셈
'''
문제
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 half,147,483,647 이하의 자연수이다.

출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
'''

## method
def sol(b,c): # a는 지수승
    if result[b] > 0 : return result[b]%c
    else:
        half = b//2
        if b%2 == 1:
            x1 = sol(half,c)
            x2 = sol(half+1,c)
            result[b] = x1*x2
        
        else :
            x1 = sol(half,c)
            x2 = sol(half,c)
            result[b] = x1*x2
        
        return result[b]%c
## input
from collections import defaultdict
A,B,C = map(int,input().split())
result = defaultdict(int) # A**key 값이 value로 저장.
result[0], result[1] = 1, A
## output
print(sol(B,C))

