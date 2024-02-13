import sys 
N = int(sys.stdin.readline())
def my_round(val):
  if val - int(val) >= 0.5:
    return int(val)+1
  else:
    return int(val)


if N == 0:
    print(0)
else:
    arr = []
    for i in range(N):
        arr.append(int(sys.stdin.readline()))

    arr.sort()

    amount = my_round(N * 0.15)
    if amount > 0:
        print(my_round(sum(arr[amount:-amount]) / (len(arr[amount:-amount]))))    
    else:
        print(my_round(sum(arr)/len(arr)))
