import functools

def compare(a, b):
    global k
    if(abs(a-k) > abs(b-k)):
        return -1
    elif abs(a-k) < abs(b-k):
        return 1
    else:
        if(a > b):
            return -1
        elif (a < b):
            return 1
        else:
            return 0

n, k = map(int, input().split())

l = []
for i in range(n):
    l.append([])

for i in range(n):
    l1 = list(map(int,input().split()))
    for j in range(n):
        l[j].append(l1[j])

# print(l)

for i in l:
    i.sort(key=functools.cmp_to_key(compare))
    i.reverse()

for i in range(n):
    for j in range(n):
        if(j < n-1):
            print(l[j][i], end = " ")
        else:
            print(l[j][i], end = "\n")