def sol(list,n):

    max_val = max(list)
    min_val = 1
    mid_val = (max_val + min_val)//2
    new_val = 0
    while 1 :
        for elem in list:
            new_val += elem // mid_val
        
        if new_val < n :
            max_val = mid_val
            mid_val = (max_val + min_val)//2
            new_val = 0
        else :
            min_val = mid_val
            mid_val = (max_val + min_val)//2
            new_val = 0
        if mid_val==min_val :
            if max_val == min_val:
                return max_val
            new_val = 0
            for e in list:
                new_val += e // max_val
            if new_val == n:
                return mid_val+1
            else :
                return mid_val

#in
k, n = map(int, input().split())
put = []
for _ in range(k):
    put.append(int(input()))

print(sol(put,n))