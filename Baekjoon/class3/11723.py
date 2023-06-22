# 집합
# add, remove, check, toggle, all, empty
import sys
M = int(sys.stdin.readline())

s = set()
for _ in range(M):

    word = sys.stdin.readline().strip()

    if word == 'all':
        s = set([i for i in range(1, 21)])
        continue
    elif word == 'empty':
        s = set()
        continue
    # print(word)
    word, num = word.split()
    num = int(num)
    if word == 'add':
        s.add(num)
    elif word == 'remove':
        s.discard(num)
    elif word == 'check':
        print(1 if num in s else 0)
    elif word == 'toggle':
        if num in s:
            s.discard(num)
        else:
            s.add(num)
