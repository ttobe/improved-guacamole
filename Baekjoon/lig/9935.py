import sys

# 입력값 처리
test = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

st = []
bomb_len = len(bomb)
for i in test:
    st.append(i)
    if bomb == ''.join(st[-bomb_len:]):
        for _ in range(bomb_len):
            st.pop()

if len(st) == 0:
    print("FRULA")
else:
    print(''.join(st))