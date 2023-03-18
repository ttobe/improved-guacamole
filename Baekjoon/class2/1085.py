# 직사각형에서 탈출

x, y, w, h = map(int, input().split())

garo = w - x
sero = h - y

if garo > x:
    garo = x
if sero > y:
    sero = y

if garo > sero:
    print(sero)
else:
    print(garo)