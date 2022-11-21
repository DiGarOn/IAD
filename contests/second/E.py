a = int(input())
b = int(input())
c = int(input())
d = int(input())

def f(a:int, b:int):
    if(a > 0):
        if(b > 0):
            return 1
        else:
            return 4
    else:
        if(b > 0):
            return 2
        else:
            return 3

if(f(a,b) == f(c,d)):
    print("YES")
else:
    print("NO")