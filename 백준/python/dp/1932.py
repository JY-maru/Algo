#정수 삼각형
#algo : dp
input_list = []
depth = int(input())
for _ in range(depth):
    sub_input = list(map(int, input().split()))
    input_list.append(sub_input)
for elem in range(1,depth):
    for idx in range(len(input_list[elem])):
        if idx == 0:
            input_list[elem][idx] += input_list[elem-1][idx]
        elif idx == len(input_list[elem]) -1 :
            input_list[elem][idx] += input_list[elem-1][idx-1]
        else :
            input_list[elem][idx] += max(input_list[elem-1][idx-1],input_list[elem-1][idx])
        
print(max(input_list[-1]))