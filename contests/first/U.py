h = int(input())
a = int(input())
b = int(input())
r = 0
s = 0
while s < h:
    s += a
    r += 1
    if(s >= h):
        break
    s -= b
print(r)