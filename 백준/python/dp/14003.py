# 가장 긴 증가하는 부분 수열 5
'''
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (-1,000,000,000 ≤ Ai ≤ 1,000,000,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

둘째 줄에는 정답이 될 수 있는 가장 긴 증가하는 부분 수열을 출력한다.
'''

## method 
def sol():
    seq = [-float('inf')]
    len_seq = 0
    record_LIS = [(-float('inf'),0)]

    for elem in arr:
        if seq[-1] < elem : 
            len_seq += 1
            record_LIS.append((elem,len_seq))
            seq.append(elem)
            
        else :
            left, right = 0, len_seq
            while left < right:
                mid = (left + right) // 2
                if seq[mid] < elem : left = mid + 1
                else : right = mid 
        
            # if right == top_idx and elem > seq[top_idx-1]:
            #     seq[right] = elem
            record_LIS.append((elem,right))
            seq[right] = elem
    # print(record_LIS)
    answer = len_seq
    answer2 = []
    for v,cnt in reversed(record_LIS):
        if answer == cnt and cnt != 0: 
            answer2.append(v)
            answer -= 1
    
    print(len_seq)
    print(' '.join(map(str,answer2[::-1])))

## input
import sys

input = sys.stdin.readline
n = int(input())
arr = [*map(int,input().split())]

## output
sol()