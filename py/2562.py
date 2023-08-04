put = []
for _ in range(9):
    put.append(int(input()))
print(max(put))
print(put.index(max(put))+1)