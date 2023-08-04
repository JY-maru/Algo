# G3
'''
문제
N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)

둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.

출력
입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.
'''
# 22 : 37 ~ 

## method
'''
def sol(num, n, k):
    search_range = n
    start_idx = 0
    slice_start = 0
    find_num = n - k
    answer = ''

    while 1 :
        search_large = num[slice_start : slice_start + search_range - find_num + 1]
        # print(search_large)
        start_idx = search_large.index(max(list(search_large)))
        slice_start += search_large.index(max(list(search_large)))
        # print(start_idx)
        answer += search_large[start_idx] #큰 수 추가
        start_idx += 1
        slice_start += 1
        search_range -= start_idx  
        find_num -= 1
        if find_num == 0 :
            return answer
'''
def sol(num, n, k):
    stack = []
    init_k = k
    for e in num :
        while stack and e > stack[-1] and init_k:
            stack.pop()
            init_k -= 1
        stack.append(e)
    if k :
        return ''.join(stack[:n-k])
    else :
        return ''.join(stack)


## input
n, k = map(int, input().split())
num = input()

## output
print(sol(num, n, k))
