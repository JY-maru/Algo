# LCS 2 
'''
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.

LCS가 여러 가지인 경우에는 아무거나 출력하고, LCS의 길이가 0인 경우에는 둘째 줄을 출력하지 않는다.
'''

## method
''' 결과는 모두 맞으나, LCS 길이와 역추적을 따로하게됨. : 시간은 느렸지만 메모리 소비량은 더 적었다.
def sol(S1,S2):
    from collections import deque

    s1, s2 = ' '+S1, ' '+S2
    l1, l2 = len(s1), len(s2)
    lcs = [[0]*l2 for _ in range(l1)]
    will_visit =deque([(l1-1,l2-1)])
    
    for i in range(1,l1):
        for j in range(1,l2):
            if s1[i] == s2[j] : lcs[i][j] = lcs[i-1][j-1] + 1
            else : lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    
    record = []

    while will_visit:
        vr,vc = will_visit.popleft()
        
        if lcs[vr][vc] == 0 : break
        if s1[vr] == s2[vc] : 
            record.append(s1[vr])
            will_visit.clear()
            will_visit.append((vr-1,vc-1))
            continue
        
        for nr,nc in [(vr-1,vc), (vr,vc-1)]:
            if lcs[nr][nc] == lcs[vr][vc]:
                will_visit.append((nr,nc))
                
    print(lcs[-1][-1])
    print(''.join(reversed(record)))
'''
def sol(S1,S2): # 시간은 빠르나 소비되는 메모리가 4배 더 크다.
    s1, s2 = ' '+S1, ' '+S2
    l1, l2 = len(s1), len(s2)
    lcs = [['']*l2 for _ in range(l1)]
    
    for i in range(1,l1):
        for j in range(1,l2):
            
            if s1[i] == s2[j] : lcs[i][j] = lcs[i-1][j-1] + s1[i]
            else :
                if len(lcs[i-1][j]) > len(lcs[i][j-1]): lcs[i][j] = lcs[i-1][j]
                else :  lcs[i][j] = lcs[i][j-1]
    print(len(lcs[-1][-1]))
    print(lcs[-1][-1])

## input 
s1 = input()
s2 = input()
## ouptut
sol(s1,s2)