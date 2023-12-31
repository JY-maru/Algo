## 숨바꼭질 4

'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
5 10 9 18 17
'''

## method
def sol(n,k):
    from collections import deque

    MIN, MAX = 0,100000
    will_visit = deque([n])
    visited_time = [float('inf')]*(MAX+1)
    visited_time[n] = 0
    prev_x = dict()

    while will_visit:
        vx = will_visit.popleft()
        if vx == k:
            break
        for nx in [vx+1, vx-1, vx*2]:
            if MIN <= nx <= MAX and visited_time[nx] > visited_time[vx] + 1:
                visited_time[nx] = visited_time[vx] + 1
                will_visit.append(nx)
                prev_x[nx] = vx

    shortestT = deque()
    tmp = k
    while tmp != n:
        shortestT.appendleft(tmp)
        tmp = prev_x[tmp]
    shortestT.appendleft(n)

    print(visited_time[k])
    print(' '.join(map(str, shortestT)))
## input 
n,k = map(int, input().split())

## output
sol(n,k)



