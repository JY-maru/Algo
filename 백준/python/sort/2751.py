'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

## method
''' quick은 최악의 경우(모두 역순정렬) O(n^2)이므로 안정성이 떨어짐. 항상 O(nlogn)인 mergesort는 괜찮을 것.
def quicksort(first,last): # index
    if first < last :
        mid = part(first, last)
        quicksort(first,mid-1)
        quicksort(mid+1, last)

def part(first,last):
    pivot = nums[last]
    smaller_part = first - 1

    for search in range(first, last):
        if nums[search] < pivot:
            smaller_part += 1
            nums[smaller_part] , nums[search] = nums[search], nums[smaller_part]
    nums[smaller_part+1], nums[last] = nums[last], nums[smaller_part+1]

    return smaller_part + 1 #pivot's index
'''
def sol(n):
    import heapq
    heapq.heapify(nums)
    for _ in range(n):
        print(heapq.heappop(nums))

#input
import sys


n = int(input())
nums = [int(sys.stdin.readline()) for _ in range(n)]

## output
# quicksort(0,len(nums)-1)
# for n in nums:
#     print(n)
sol(n)