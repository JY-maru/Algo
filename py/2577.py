from collections import defaultdict
nums = 1
for _ in range(3):
    nums *= int(input())

cnt = defaultdict(int)
for i in str(nums):
    cnt[int(i)] += 1
cnt =dict(sorted(cnt.items(), key = lambda x : x[0]))

for i in range(10):
    try : 
        print(cnt[i])
    except :
        print(0)