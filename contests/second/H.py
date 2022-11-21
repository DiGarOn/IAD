a = int(input())
b = int(input())
c = int(input())

s1 = 0
s2 = 0
if(a % 2 == 0):
    s2 += 1
else:
    s1 += 1

if(b % 2 == 0):
    s2 += 1
else:
    s1 += 1
if(c % 2 == 0):
    s2 += 1
else:
    s1 += 1

if(s1 == 0 or s2 == 0):
    print("NO")
else:
    print("YES")