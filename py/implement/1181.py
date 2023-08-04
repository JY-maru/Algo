#자료구조 : 해시테이블(dict)
#우선순위 1 : 단어길이를 key로 하여 data생성
#우선순위 2 : 같은 단어 길이에서는 사전 순으로 출력하기 위해 sort

def word_sort(words):
    from collections import defaultdict
    cnt = defaultdict(list)
    for elem in words:
        cnt[len(elem)].append(elem) 
    cnt = dict(sorted(cnt.items(),key = lambda x : x[0]))
    for k in cnt.keys():
        cnt[k].sort()
        for w in cnt[k]:
            print(w)
            
#in
num = int(input())
words = [input() for _ in range(num)]
words = list(set(words))

#out
word_sort(words)