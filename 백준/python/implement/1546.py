# 평균 조작하기

num = int(input())
score = list(map(int,input().split()))
max_s = max(score)
fixed_scr = [x/max_s*100 for x in score]
print(sum(fixed_scr)/num)