# 연결 요소 개수 
'''
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ Nx(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.
'''

#####idea#####
# dfs : 간선 수가 많을 때 recursionError
# 백준에선 입력받을 시, input() 대신 sys.stdin.readline()

from collections import deque
import sys
##oper
def bfs(s):
    willVisit.append(s)
    visit[s] = 1 #방문 표시
    while willVisit:
        visiting = willVisit.popleft()
        # 인접노드 추가시 방문한 노드와의 중복 주의
        for adj_nodes in graph[visiting]:
            if visit[adj_nodes] == 0:
                visit[adj_nodes] = 1
                willVisit.append(adj_nodes)
         
        
def sol(N,M): #노드별 bfs 실시
    cnt = 0
    while 0 in visit:
        start_idx = visit.index(0)
        bfs(start_idx)
        cnt += 1
    return cnt


##input
N, M = map(int, input().split(' '))
visit = [0 if i != 0 else 1 for i in range(N+1)] # 노드별 방문 여부 표시
graph = [[] for _ in range(N+1)] # 노드별 이웃노드 정리
willVisit = deque()
for idx in range(M):
    nodes = list(map(int, sys.stdin.readline().split(' ')))
    graph[nodes[0]].append(nodes[1])
    graph[nodes[1]].append(nodes[0])

##output
print(sol(N,M))