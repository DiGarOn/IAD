n = int(input())

d = set()
for i in range(n):
    d.update([input()])
w = set(map(str,input().split()))
s = 0
w = w.difference(d)
for i in w:
    if(i.lower() in [i.lower() for i in d]):
        s += 1
        continue
    if(i.lower() == i):
        s += 1
        continue
    else:
        k = 0
        for j in i:
            if(j != j.lower()):
                k += 1
                if(k>1):
                    break
        if(k > 1):
            s += 1
            continue
print(s)