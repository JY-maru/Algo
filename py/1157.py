#가장 많이 중복되는 단어 찾기 -> 대문자로 출력
#
from collections import defaultdict
str = input().lower()
cnt = defaultdict(int)
for ch in str:
    cnt[ch] += 1
cnt = dict(sorted(cnt.items(),key = lambda x : x[1],reverse = True))

if len(list(cnt.keys())) > 1 and cnt[list(cnt.keys())[0]] == cnt[list(cnt.keys())[1]]:
    print('?')
else :
    print(list(cnt.keys())[0].upper())