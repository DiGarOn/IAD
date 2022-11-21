x = int(input())
y = int(input())

if(x%(y-x+1)==1):
    print("YES")
else:
    print("NO")