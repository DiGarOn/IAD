n = int(input())
d = {}
for i in range(n):
    l = list(map(str,input().split()))
    for j in range(1,len(l)):
        d[l[j]] = l[0]
n = int(input())
for i in range(n):
    print(d[input()])