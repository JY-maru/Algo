'''
문제
n(1≤n≤1,000)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라. 항상 시작점에서 도착점으로의 경로가 존재한다.

입력
첫째 줄에 도시의 개수 n(1≤n≤1,000)이 주어지고 둘째 줄에는 버스의 개수 m(1≤m≤100,000)이 주어진다. 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 m+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.

출력
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

둘째 줄에는 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력한다. 출발 도시와 도착 도시도 포함한다.

셋째 줄에는 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력한다.
'''

## method
def sol(s,e):
    from collections import defaultdict,deque
    import heapq
    updated_w = defaultdict(lambda : float('inf'))
    
    will_visit = [(s,0)]

    while will_visit:
        vu, vw = heapq.heappop(will_visit)

        for adjv, adjw in graph[vu]:
            if updated_w[adjv] > vw + adjw : # v 와 u + w 비교
                updated_w[adjv], prev_u[adjv]= vw + adjw, vu
                heapq.heappush(will_visit,(adjv, updated_w[adjv]))
                
    
    shortest_path = deque()
    tmp = e
    cnt = 0
    while tmp != s:
        cnt += 1
        shortest_path.appendleft(tmp)
        tmp = prev_u[tmp]
    shortest_path.appendleft(s)

    ## output
    print(updated_w[e])
    print(cnt +1 )
    print(' '.join(map(str, shortest_path)))

## input
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]  

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
start, end = map(int, input().split())
prev_u = [start]*(n+1) # v의 이전노드 기록 (u)

## output
sol(start,end)
