'''
문제
어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 팰린드롬이라 부른다. 예를 들어 79,197과 324,423 등이 팰린드롬 수이다.

어떤 수 N (1 ≤ N ≤ 1,000,000)이 주어졌을 때, N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다.

출력
첫째 줄에 조건을 만족하는 수를 출력한다.
'''

## method
def check_p(num):
    for i in range(len(str(num))//2):
            if str(num)[i] != str(num)[-(i+1)]: # [::-1]
                return False
    return True

def check_prime(num):
    import math
    if num == 1: return False

    p = [2]
    for n in range(3, int(math.sqrt(num))+1):
        if 0 not in [n%i for i in p]:
            p.append(n)
            continue

    if 0 not in [num%i for i in p] or num in p:
        return True
    else: return False

def sol(n):
    import math
    num = n
    
    while 1:
        if check_p(num) and check_prime(num):
            return num
        num += 1
        
## input
n = int(input())
## output
print(sol(n))