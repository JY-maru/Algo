# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이


def sol(put,N):
    import math
    from collections import Counter
    
    result1 = sum(put) / N
    #1
    if result1 >= 0:
        print(int(result1 + 0.5))
    else :
        print(int(result1 - 0.5))
    
    #2
    put.sort()
    print(put[N//2])
    
    #3
    cnt = Counter(put).most_common()
    if len(cnt) > 1 and cnt[0][1] == cnt [1][1] :
        print(cnt[1][0])
    else:
        print(cnt[0][0])
    #4
    print(max(put) - min(put))

import sys
#in
N = int(input())
put = []
for _ in range(N):
    num = int(sys.stdin.readline())
    put.append(num)
sol(put,N)
