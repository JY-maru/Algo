#dfs와 bfs
#graph별(인접 노드 별) 정렬을 안해주어서 계속 틀렸던 것 ㅡㅡ..;
from collections import defaultdict,deque

def bfs(graph,start):
    will_visit = deque([start])
    while will_visit:
        visiting = will_visit.popleft() 
        print(visiting, end=' ')
        visit_check[visiting] = 1 #현재 방문 노드 방문 표시
        for elem in graph[visiting]: #another way for adding neighbor node
            if not visit_check[elem] :
                will_visit.append(elem)
                visit_check[elem] = 1 #인접 노드 방문 표시 : will_visit에 중복되어 들어가지 않기 위함.
    
def dfs(graph,start,visited=[]):
    visited.append(start)
    print(start, end = ' ')
    for node in graph[start]:
        if node not in visited :
            dfs(graph,node,visited)
    

input_list = list(map(int,input().split())) # idx 0: 노드수, 1: 간선 수, 2: 출발 node
graph = defaultdict(list)
visit_check = [0 for _ in range(input_list[0]+1)]
for _ in range(input_list[1]):
    edge = list(map(int,input().split()))
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

for i in range(1,input_list[0]+1):    
    graph[i] = sorted(graph[i])

dfs(graph, input_list[2])
print()
bfs(graph, input_list[2])
