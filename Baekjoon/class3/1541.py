import sys

line = sys.stdin.readline().strip()
line += " "
now = ""
result = 0
minus_sum = 0
minus_flag = False
k = 0
for i in range(len(line)):
    if line[i].isdigit() and i != len(line) - 1:
        now += line[i]
    else:
        k = int(now)
        if line[i] == "-" and minus_flag == False:
            result += k
            minus_flag = True
        elif line[i] == "-" and minus_flag == True:
            result -= k
            result -= minus_sum
            minus_sum = 0   
        elif line[i] == "+" and minus_flag == False:
            result += k
            minus_flag = False
        elif line[i] == "+" and minus_flag == True:
            minus_sum += k
        now = ""

if minus_flag == False:
    result += k
elif minus_flag == True:
    result -= k
    result -= minus_sum    

print(result)