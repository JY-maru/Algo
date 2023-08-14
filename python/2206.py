'''
문제
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
'''

## method
def sol(maps,R,C):
    from collections import deque
    
    visited = [[[0]*2 for _ in range(C)] for _ in range(N)] #부수지 않은 상태 : 0, 부순 상태 : 1
    
    r = (1,-1, 0, 0)
    c = (0,0, 1, -1)

    will_visit = deque([(0,0,0)])
    visited[0][0][0] = 1

    while will_visit:
        vr, vc, broken = will_visit.popleft()
        
        if vr == R-1 and vc == C-1 :
            return visited[vr][vc][broken]

        for dr, dc in zip(r,c):
            nr, nc = vr+dr, vc+dc
            if 0<=nr<R and 0<=nc<C :
                # 벽만났을 때 부셔보기. 부셔보고, 완주 못하면 알아서 소멸되기 때문
                if maps[nr][nc] == 1 and broken==0 :
                    visited[nr][nc][1] = visited[vr][vc][0] + 1
                    will_visit.append((nr,nc,1))
                
                # 갈 수 있고, 방문가능 한 곳
                elif maps[nr][nc] == 0 and visited[nr][nc][broken] == 0:
                    visited[nr][nc][broken] = visited[vr][vc][broken] + 1
                    will_visit.append((nr,nc,broken))
    
    return -1

## input
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
maps = [list(map(int,list(input().rstrip('\n')))) for _ in range(N)]

## output
print(sol(maps,N,M))
