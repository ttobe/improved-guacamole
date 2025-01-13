import sys

N = int(sys.stdin.readline())
tree = {chr(i):['.', '.'] for i in range(65, 65+N)}

for _ in range(N):
    a, b, c = sys.stdin.readline().split()
    if b != '.':
        tree[a][0] = b

    if c != '.':
        tree[a][1] = c

def first(now):
    print(now, end="")

    if tree[now][0] != '.':
        first(tree[now][0])
    if tree[now][1] != '.':
        first(tree[now][1])

def mid(now):

    if tree[now][0] != '.':
        mid(tree[now][0])
    print(now, end="")
    if tree[now][1] != '.':
        mid(tree[now][1])

def end(now):

    if tree[now][0] != '.':
        end(tree[now][0])
    if tree[now][1] != '.':
        end(tree[now][1])
    print(now, end="")


first('A')
print()
mid('A')
print()
end('A')