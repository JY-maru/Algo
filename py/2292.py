def bee(num):
    cnt = 0
    while 1 :
        if 6*cnt + 2 <= num and  6*(cnt+1) -1 +6*cnt + 2 >= num:
            break
        cnt += 1
    return cnt + 2


n = int(input())
print(bee(n))