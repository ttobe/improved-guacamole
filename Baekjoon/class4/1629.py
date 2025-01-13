def sol(A, B, C):
    t = 1
    tmp = 1
    while True:
        if t == B:
            return tmp
        if t * 2 <= B:
            tmp = (tmp * tmp) % C
            t *= 2
        else:
            tmp = (tmp * A) % C
            t += 1
import sys

A, B, C = map(int, sys.stdin.readline().split())

print(pow(A, B, C ))