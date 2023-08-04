#w,h로 형성된 사각형내에 (x,y)로 이루어져 있다. 이때 이 사각형을 탈출할 수 있는 최단경로 길이 출력하기.
x,y,w,h = map(int,input().split())
shortest = [x,y,w-x,h-y]
print(min(shortest))