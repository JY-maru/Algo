def check(str):
    store = []
    group = ''
    for char in str :
        if char == group :
            continue
        if char not in store  :
            store.append(char)
            group = char
        
        else :
            return False
    return True

num = int(input())
cnt = 0
for i in range(num) :
    string = input()
    if check(string) :
        cnt += 1
    
print(cnt)
