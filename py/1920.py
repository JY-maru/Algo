# n배열에 m값이 있는지 확인하기

def sol(nums,find):
    from collections import defaultdict
    check = defaultdict(int)
    for n in nums:
        check[n] = 1
    
    for m in find:
        print(check[m])

#in
N = int(input())
nums = list(map(int,input().split()))
M = int(input())
find_nums = list(map(int,input().split()))

#out
sol(nums,find_nums)