# N과 M(1)
'''
문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''

## method
def sol(k):# k는 택한 수의 개수
    global n, m
    if k == m: 
        for s in range(m):
            print(seq[s], end=' ')
        print()
        return

    for i in range(1,n+1): # 1~n 까지의 수 중에서 탐색
        if not used[i]:
            seq[k] = i
            used[i] = True
            sol(k+1)
            used[i] = False
            
## input
n, m = map(int,input().split())
seq = [0]*(n+1)
used = [False]*(n+1)
## output
sol(0)