n = int(input())
l = list(map(int,input().split()))
s = 0
# print(l)
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if((l[i]+l[j]>l[k]) and (l[i]+l[k]>l[j]) and (l[k]+l[j]>l[i])):
                s += 1

print(s)