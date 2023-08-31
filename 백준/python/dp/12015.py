# 가장 긴 증가하는 부분 수열 2
'''
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
'''
# [0,3,...] 이런 memo에 top보다 큰 원소는 추가, 아닌 원소들은 기존 memo에 추가할 적합한 자리를 찾으며
## method
def sol():
    memo = [0]

    for elem in arr:
        if elem > memo[-1] : memo.append(elem)
        else : # 들어가서 바꿀 자리 찾음
            left = 0
            right = len(memo) # 탐색 길이 만큼

            while left < right:
                mid = (left+right) // 2

                if memo[mid] < elem:
                    left = mid + 1
                else :
                    right = mid # 탐색 길이 만큼
            memo[right] = elem
    
    return len(memo) -1

## input
N = int(input())
arr = list(map(int,input().split()))
## output
print(sol())
