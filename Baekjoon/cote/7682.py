# 틱텍토

# 입력
# 9줄의 문자 X, ), .하나

import sys
from collections import Counter

bingo_cond = [
    # 가로
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    # 세로
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    # 대각
    [0, 4, 8],
    [2, 4, 6]
]

def bingo(line, what):
    for cond in bingo_cond:
        a, b, c = cond
        if line[a] == line[b] == line[c] == what != ".":
            return cond
    
    return []


while True:
    line = sys.stdin.readline().strip()

    if line == "end":
        break
    
    c = Counter(line)
    cx = c["X"]
    co = c["O"]
    if "X" not in c and "O" not in c:
        print("invalid")
        continue

    # O의 수가 X보다 많다.
    if co > cx:
        print("invalid")
        continue
    # X의 수가 O의 수 보다 2 이상 차이난다.
    if cx > co + 1:
        print("invalid")
        continue
    cond_X = bingo(line, "X")
    cond_O = bingo(line, "O")
    if cx == co:
        if cond_O and not cond_X:
            print("valid")
            continue
    if co + 1 == cx:
        if cond_X and not cond_O:
            print("valid")
            continue
    # 빙고시 X 가 빙고일 때 O가 X와 같다면 안됨
    if cx == 5 and co == 4:
        if not cond_O:
            print("valid")
            continue
    
    print("invalid")

