'''
문제
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

입력
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

출력
첫째 줄에 정답을 출력한다.
'''

###idea
# 모두 + 또는 모두 - : 앞뒤 괄호
# + 이후 - : 괄호가 +로 묶이므로 값변화 x
# - 이후 + : 괄호안의 연산값이 음수로 바뀜
# 따라서 - + + - 사이의 +항들까지를 괄호로 묶어 연산하는 방안
# 00002 이런 숫자들 때문에 eval안쓰고 해봄

import re
## method
def str2oper(strn): # 숫자 + 연산자 조합의 str타입을 연산해주는 메소드
    opers = [s for s in strn if s in ('+','-')]
    nums = list(map(int ,re.sub( '[+,-]', ' ', strn).split()))
    result = nums[0]
    for i in range(len(opers)):
        if opers[i] == '+':
            result += nums[i+1]
        else :
            result -= nums[i+1]
    return str(result)

def sol(oper):
    for i in range(len(oper)):
        oper[i] = str2oper(oper[i])
    result = '-'.join(oper)
    
    return str2oper(result)
## input
dif_oper = input().split('-') # 원소끼리 -연산

## output
print(sol(dif_oper))