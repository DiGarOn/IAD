n = int(input())
l = list(map(int, input().split()))

def check(start:int):
    global l,n
    k = 1
    for j in range(start, (n+start)//2):
        if(l[j] != l[n-k]):
            return False
        k += 1
    return True

flag = False
for i in range(n):
    if(l[i] == l[n-i-1]):
        if(check(i)):
            print(i)
            print(*reversed(l[:i]))
            flag = True
            break
if(not flag):
    print(n-1)
    print(*reversed(l[:n-1]))
