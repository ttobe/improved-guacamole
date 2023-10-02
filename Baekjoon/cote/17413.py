# 단어 뒤집기

s = input()
arr = []

state = False
for i in range(len(s)):
    if s[i] == '<':
        state = True
        if len(s) > 0:
            for j in reversed(range(len(arr))):
                print(arr[j], end='')

            arr.clear()
    elif s[i] == '>':
        print("<", end='')
        for j in range(len(arr)):
            print(arr[j], end='')
        print(">", end='')
        state = False
        arr.clear()
    
    elif s[i] == ' ' and state == False:
        for j in reversed(range(len(arr))):
            print(arr[j], end='')
        print(" ", end='')
        arr.clear()
    else: 
        arr.append(s[i])


for j in reversed(range(len(arr))):
    print(arr[j], end='')
