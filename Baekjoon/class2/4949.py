# 균형잡힌 세상

while True:
    arr = input()
    result = True
    # print(arr)
    if arr == '.':
        # print('yes')
        break
    stack = []
    for i in range(len(arr)):
        if arr[i] == '[' or arr[i] == '(':
            stack.append(arr[i])
        elif arr[i] == ']':
            if len(stack) == 0 or stack[-1] == '(':
                result = False
                break
            elif stack[-1] == '[':
                stack.pop()
        elif arr[i] == ')':
            if len(stack) == 0 or stack[-1] == '[':
                result = False
                break
            elif stack[-1] == '(':
                stack.pop()
# print(stack)
    if len(stack) != 0 or result == False:
        print('no') 
    else:
        print('yes')