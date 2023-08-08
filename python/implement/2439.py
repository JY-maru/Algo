def star(num):
    for i in range(1,num+1):
        star = '*'*i
        print(star.rjust(num))
num = int(input())
star(num)