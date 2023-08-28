'''
문제
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
'''

## method
def sol():
    import sys
    from collections import defaultdict,deque
    size = int(sys.stdin.readline())
    s_x ,s_y = map(int, sys.stdin.readline().split())
    d_x ,d_y = map(int, sys.stdin.readline().split())

    if s_x == d_x and s_y == d_y:
        return 0
    
    unit = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    go_to = defaultdict(list)
    go_to[0].append([s_x, s_y])
   
    arrived = deque([(s_x, s_y)])
    
    # 방문 체크 및 깊이 기록 : -1 방문 x
    visited = [[-1] * size for _ in range(size)]
    visited[s_x][s_y] = 0
    
    while arrived:
        vx, vy = arrived.popleft()

        for u in unit:  
            nx, ny = vx + u[0], vy + u[1]
            
            if nx >= 0 and ny >= 0 and  nx < size and ny < size:
                if visited[nx][ny] != -1: # 방문했을 때
                    continue
                arrived.append((nx,ny))
                visited[nx][ny] = visited[vx][vy] + 1

            if nx == d_x and ny == d_y:
                return visited[nx][ny]
        
## input
n = int(input())
## output
for _ in range(n):
    print(sol())