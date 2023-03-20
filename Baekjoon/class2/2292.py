# 벌집?

# 6, 12, 18, 24 ...
import math
N = int(input())

test = 1
result = 1

while(True):
    if N <= test:
        print(result)
        break
    else:
        test += 6 * result
        result += 1