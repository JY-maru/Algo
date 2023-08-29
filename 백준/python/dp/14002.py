# 가장 긴 증가하는 수열 4
'''
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.
'''
# 50 40 10  20 30 25 40
## method
def sol(N):
    dp = [1]*N
    answer = []
    for i in range(1,N):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[j]+1, dp[i]) 
    
    search_elem = max(dp)
    print(search_elem)

    for i in range(N-1,-1,-1):
        if search_elem == 0: break
        if dp[i] == search_elem:
            answer.append(arr[i])
            search_elem -= 1

    print(' '.join(map(str,reversed(answer))))

## input
N = int(input())
arr = list(map(int,input().split()))
## output 
sol(N)